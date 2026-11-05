# coding: utf-8
import json
import sys

from tccli import sso
from tccli.plugins.sso import texts, configs, terminal
from tccli.plugins.sso.texts import get as _


def print_message(msg):
    print(msg)
    sys.stdout.flush()


def _load_session(profile):
    """读取 SSO 登录态, 无效时打印提示并返回 None。"""
    session = sso.load_login_token(profile)
    if not session:
        print_message(_("list_login_expired"))
    return session


def _print_json(data):
    print_message(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def list_uin_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language") or configs.DEFAULT_LANG
    texts.set_lang(language)
    profile = parsed_globals.get("profile") or "default"

    session = _load_session(profile)
    if not session:
        return

    accounts = sso.list_accounts_for_access_assignment(session["token"], session["site"])
    if not accounts:
        print_message(_("list_no_account"))
        return

    result = [{"Uin": str(x["Uin"]), "Name": x.get("Name", "")} for x in accounts]

    if args.get("output") == "json":
        _print_json(result)
        return

    print_message("%-20s %s" % ("UIN", "NAME"))
    for x in result:
        print_message("%-20s %s" % (x["Uin"], x["Name"]))
    print_message("")
    print_message("total: %d" % len(result))


def list_role_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language") or configs.DEFAULT_LANG
    texts.set_lang(language)
    profile = parsed_globals.get("profile") or "default"

    session = _load_session(profile)
    if not session:
        return

    uin = args.get("uin", "")
    if not uin:
        uin = _pick_uin(session)
        if not uin:
            return

    roles = sso.list_role_configurations_for_account(uin, session["token"], session["site"])
    if not roles:
        print_message(_("no_role"))
        return

    result = [{
        "Uin": uin,
        "RoleConfigurationName": x.get("RoleConfigurationName", ""),
        "RoleConfigurationId": x.get("RoleConfigurationId", ""),
    } for x in roles]

    if args.get("output") == "json":
        _print_json(result)
        return

    print_message("%-40s %s" % ("ROLE_NAME", "ROLE_CONFIGURATION_ID"))
    for x in result:
        print_message("%-40s %s" % (x["RoleConfigurationName"], x["RoleConfigurationId"]))
    print_message("")
    print_message("uin: %s, total: %d" % (uin, len(result)))


def _pick_uin(session):
    """未指定 --uin 时, 用交互选择的方式让用户挑一个账号。"""
    accounts = sso.list_accounts_for_access_assignment(session["token"], session["site"])
    if not accounts:
        print_message(_("list_no_account"))
        return ""

    uins = [str(x["Uin"]) for x in accounts]
    idx = terminal.select_from_items(
        _("account_select_prompt"), ["%s:%s" % (x.get("Name", ""), x["Uin"]) for x in accounts], 10, 0)
    return uins[idx]
