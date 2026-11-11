# coding: utf-8
import sys

from tccli import sso
from tccli.plugins.sso import texts, configs, terminal
from tccli.plugins.sso.texts import get as _


def print_message(msg):
    print(msg)
    sys.stdout.flush()


def print_error(msg):
    """提示信息走 stderr, 不混进管道里的数据输出。"""
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


# 与 main.py 保持一致的错误码约定: 非 0 表示命令失败, 脚本据此中断遍历
_EXIT_FAILURE = 255


def _fail(msg):
    """打印错误并以非 0 退出码结束命令。

    tccli 的 main() 不采用 action_caller 的返回值, 所以这里抛 SystemExit 让进程带上退出码,
    上层脚本才能把失败和"查到了 0 条"区分开。SystemExit 不会被 main() 里的 except 捕获。
    """
    print_error(msg)
    raise SystemExit(_EXIT_FAILURE)


def _stdin_is_terminal():
    """stdin 是否连着终端; 非终端时不能进交互选择。"""
    try:
        return sys.stdin.isatty()
    except Exception:
        return False


def _load_session(profile):
    """读取 SSO 登录态, 无效时打印提示并以失败退出码结束。"""
    session = sso.load_login_token(profile)
    if not session:
        _fail(_("list_login_expired"))
    return session


def _print_rows(rows):
    """逐行输出制表符分隔的记录, 便于 cut/awk/while read 直接消费。

    不输出表头与统计行, 方便脚本无脑遍历; 表头说明由 help 承载。
    """
    for row in rows:
        print_message("\t".join(row))


def list_uin_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language") or configs.DEFAULT_LANG
    texts.set_lang(language)
    profile = parsed_globals.get("profile") or "default"

    session = _load_session(profile)

    accounts = sso.list_accounts_for_access_assignment(session["token"], session["site"])
    if not accounts:
        _fail(_("list_no_account"))

    # 每行: <uin>\t<name>
    _print_rows([[str(x["Uin"]), x.get("Name", "")] for x in accounts])
    return 0


def list_role_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language") or configs.DEFAULT_LANG
    texts.set_lang(language)
    profile = parsed_globals.get("profile") or "default"

    session = _load_session(profile)

    uin = args.get("uin", "")
    if not uin:
        if not _stdin_is_terminal():
            _fail(_("uin_required_when_not_terminal"))
        uin = _pick_uin(session)
        if not uin:
            # _pick_uin 已经打印过原因, 这里只需要带上失败退出码
            raise SystemExit(_EXIT_FAILURE)
    else:
        try:
            uin = int(uin)
        except ValueError:
            _fail(_("invalid_uin") % uin)

    roles = sso.list_role_configurations_for_account(uin, session["token"], session["site"])
    if not roles:
        _fail(_("no_role"))

    # 每行: <uin>\t<role name>\t<role configuration id>
    # 同一 role 在不同 uin 下 id 不同, 按需求不去重, uin 与 role id 必须一起输出
    _print_rows([
        [str(uin), x.get("RoleConfigurationName", ""), x.get("RoleConfigurationId", "")]
        for x in roles
    ])
    return 0


def _pick_uin(session):
    """未指定 --uin 时, 用交互选择的方式让用户挑一个账号。"""
    accounts = sso.list_accounts_for_access_assignment(session["token"], session["site"])
    if not accounts:
        print_error(_("list_no_account"))
        return None

    idx = terminal.select_from_items(
        _("account_select_prompt"), ["%s:%s" % (x.get("Name", ""), x["Uin"]) for x in accounts], 10, 0)
    # 返回整数 uin: TargetUin 在 CIC 侧是 int64, 这里不转后面就会把字符串发出去
    return int(accounts[idx]["Uin"])
