# coding: utf-8
import json
import os.path
import random
import string
import sys
import time
import uuid
import webbrowser

from six.moves.urllib.parse import urlencode

from tccli import sso
from tccli.plugins.sso import texts, terminal, configs
from tccli.plugins.sso.texts import get as _

_DURATION_MIN = 1800
_DURATION_MAX = 43200
_DURATION_DEFAULT = 7200
# 服务端表示登录态已失效的错误码关键字
_AUTH_ERROR_KEYWORD = "JWTVerifyFailed"
_SESSION_FALLBACK_DUR = 3600 * 12


def print_message(msg):
    print(msg)
    sys.stdout.flush()


def login_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = configs.DEFAULT_LANG
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    login(args, profile, language)


def login(args, profile, language):
    duration = args.get("duration", _DURATION_DEFAULT)
    if not (_DURATION_MIN <= duration <= _DURATION_MAX):
        print_message(_("invalid_duration") % duration)
        return

    cred_path = sso.cred_path_of_profile(profile)
    auth_url = ""
    last_uin = ""
    last_role = ""
    if os.path.exists(cred_path):
        with open(cred_path, "r") as cred_file:
            cred_data = json.load(cred_file)
            sso_data = cred_data.get("sso", {})
            auth_url = sso_data.get("authUrl", "")
            last_uin = str(sso_data.get("uin", ""))
            last_role = sso_data.get("roleConfigurationName", "")

    if not auth_url:
        profile_opt = ""
        if profile != "default":
            profile_opt = "--profile %s " % profile
        print_message(_("auth_url_not_configured") % profile_opt)
        return

    cached = sso.load_login_token(profile)
    if cached:
        print_message(_("login_token_valid") % ((cached["expiresAt"] - time.time()) / 60))
        token = {"Token": cached["token"], "Site": cached["site"], "State": ""}
    else:
        print_message(_("token_expired_relogin"))
        token = _browser_login(auth_url, language)

    print_message("")

    login_token = token["Token"]
    site = token["Site"]
    try:
        accounts = sso.list_accounts_for_access_assignment(login_token, site)
    except ValueError as e:
        # 本地缓存还没过期, 但服务端已吊销该登录态: 清掉缓存并回退到浏览器登录
        if not cached or not _is_auth_error(e):
            raise
        print_message(_("login_state_revoked"))
        token = _browser_login(auth_url, language)
        login_token = token["Token"]
        site = token["Site"]
        accounts = sso.list_accounts_for_access_assignment(login_token, site)
    if not accounts:
        print_message(_("no_account"))
        return

    specified_uin = args.get("uin", "")
    if specified_uin:
        account = next((x for x in accounts if str(x["Uin"]) == specified_uin), None)
        if not account:
            print_message(_("specified_uin_not_found") % (specified_uin, ",".join(str(x["Uin"]) for x in accounts)))
            return
    else:
        default_idx = next((i for i, x in enumerate(accounts) if str(x["Uin"]) == last_uin), 0)
        idx = terminal.select_from_items(
            _("account_select_prompt"), ["%s:%s" % (x["Name"], x["Uin"]) for x in accounts], 10, default_idx)
        account = accounts[idx]

    print_message("uin: %s" % account["Uin"])
    print_message("username: %s" % account["Name"])

    roles = sso.list_role_configurations_for_account(account["Uin"], login_token, site)
    if not roles:
        print_message(_("no_role"))
        return

    specified_role = args.get("rolename", "")
    specified_role_id = args.get("role-id", "")
    if specified_role_id:
        role = next((x for x in roles if x["RoleConfigurationId"] == specified_role_id), None)
        if not role:
            print_message(
                _("specified_role_not_found") % (specified_role_id, ",".join(x["RoleConfigurationId"] for x in roles)))
            return
    elif specified_role:
        role = next((x for x in roles if x["RoleConfigurationName"] == specified_role), None)
        if not role:
            print_message(
                _("specified_role_not_found") % (specified_role, ",".join(x["RoleConfigurationName"] for x in roles)))
            return
    else:
        default_idx = 0
        if str(account["Uin"]) == last_uin:
            default_idx = next((i for i, x in enumerate(roles) if x["RoleConfigurationName"] == last_role), 0)
        idx = terminal.select_from_items(
            _("role_select_prompt"), [x["RoleConfigurationName"] for x in roles], 10, default_idx)
        role = roles[idx]

    print_message("role: %s" % role["RoleConfigurationName"])
    print_message("role id: %s" % role["RoleConfigurationId"])

    saml_resp = sso.gen_saml_response(
        login_token, "RoleSAML", account["Uin"], "", role["RoleConfigurationId"], site)

    token_info = sso.verify_login_skey(login_token, site)

    # 登录态有效期优先取服务端返回值, 拿不到时按 _SESSION_FALLBACK_DUR 兜底
    if cached:
        sso_expires_at = cached["expiresAt"]
    else:
        sso_expires_at = int(token_info.get("ExpiresAt") or 0) or int(time.time()) + _SESSION_FALLBACK_DUR

    role_arn = "qcs::cam::uin/%s:roleName/TencentCloudSSO-%s" % (account["Uin"], role["RoleConfigurationName"])
    principal_arn = "qcs::cam::uin/%s:saml-provider/TencentReservedSSO-%s" % (account["Uin"], token_info["ZoneId"])
    cred = sso.assume_role_with_saml(
        saml_resp["SAMLResponse"], principal_arn, role_arn, "ses-%s" % uuid.uuid4(), duration, site)

    sso_info = {
        "token": login_token,
        "uin": account["Uin"],
        "roleConfigurationId": role["RoleConfigurationId"],
        "roleConfigurationName": role["RoleConfigurationName"],
        "zoneId": token_info["ZoneId"],
        "site": site,
        "authUrl": auth_url,
        "expiresAt": sso_expires_at,
    }
    sso.save_credential(cred, sso_info, profile, login_token)

    print_message(_("login_success") % sso.cred_path_of_profile(profile))
    # 打印 uin/role/role id, 便于直接拿去 sso list-role --uin
    print_message(_("login_result") % (account["Uin"], role["RoleConfigurationName"], role["RoleConfigurationId"]))


def _browser_login(auth_url, language):
    """打开浏览器等待用户点击同意, 返回登录态。"""
    characters = string.ascii_letters + string.digits
    state = ''.join(random.choice(characters) for x in range(32))

    token = _get_token(auth_url, state, language)

    if token["State"] != state:
        raise ValueError("invalid state %s" % token["state"])

    return token


def _is_auth_error(exc):
    """判断异常是否为服务端拒绝登录态(区别于网络错误)。"""
    return _AUTH_ERROR_KEYWORD in str(exc)

def _get_token(auth_url, state, language):
    cli_params = {
        "lang": language,
        "site": configs.SITE,
        "state": state,
    }
    cli_query = urlencode(cli_params)
    cli_url = configs.CLI_URL + "?" + cli_query
    url_params = {
        "loginType": "tccli",
        "callback": cli_url,
        "state": state,
    }
    url_query = urlencode(url_params)
    auth_url = auth_url + "?" + url_query

    print_message(_("try_login_with_url"))
    print_message("")
    print_message(auth_url)

    webbrowser.open(auth_url)

    while True:
        time.sleep(1)

        login_state = sso.check_login_state(state)
        if "Error" in login_state:
            raise ValueError(login_state["Error"])

        if login_state["Status"] == "NotFound":
            continue

        if login_state["Status"] == "Finished":
            return login_state["Token"]

        raise ValueError("invalid resp: %s" % login_state)
