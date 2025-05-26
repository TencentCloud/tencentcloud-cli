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
    cred_path = sso.cred_path_of_profile(profile)
    auth_url = ""
    if os.path.exists(cred_path):
        with open(cred_path, "r") as cred_file:
            cred_data = json.load(cred_file)
            auth_url = cred_data.get("sso", {}).get("authUrl", "")

    if not auth_url:
        profile_opt = ""
        if profile != "default":
            profile_opt = "--profile %s " % profile
        print_message(_("auth_url_not_configured") % profile_opt)
        return

    characters = string.ascii_letters + string.digits
    state = ''.join(random.choice(characters) for x in range(32))

    token = _get_token(auth_url, state, language)

    if token["State"] != state:
        raise ValueError("invalid state %s" % token["state"])

    print_message("")

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
        idx = terminal.select_from_items(
            _("account_select_prompt"), ["%s:%s" % (x["Name"], x["Uin"]) for x in accounts], 10)
        account = accounts[idx]

    print_message("uin: %s" % account["Uin"])
    print_message("username: %s" % account["Name"])

    roles = sso.list_role_configurations_for_account(account["Uin"], login_token, site)
    if not roles:
        print_message(_("no_role"))
        return

    specified_role = args.get("rolename", "")
    if specified_role:
        role = next((x for x in roles if x["RoleConfigurationName"] == specified_role), None)
        if not role:
            print_message(
                _("specified_role_not_found") % (specified_role, ",".join(x["RoleConfigurationName"] for x in roles)))
            return
    else:
        idx = terminal.select_from_items(
            _("role_select_prompt"), [x["RoleConfigurationName"] for x in roles], 10)
        role = roles[idx]

    print_message("role: %s" % role["RoleConfigurationName"])

    saml_resp = sso.gen_saml_response(
        login_token, "RoleSAML", account["Uin"], "", role["RoleConfigurationId"], site)

    token_info = sso.verify_login_skey(login_token, site)

    role_arn = "qcs::cam::uin/%s:roleName/TencentCloudSSO-%s" % (account["Uin"], role["RoleConfigurationName"])
    principal_arn = "qcs::cam::uin/%s:saml-provider/TencentReservedSSO-%s" % (account["Uin"], token_info["ZoneId"])
    cred = sso.assume_role_with_saml(
        saml_resp["SAMLResponse"], principal_arn, role_arn, "ses-%s" % uuid.uuid4(), args.get("duration", 7200), site)

    sso_info = {
        "token": login_token,
        "uin": account["Uin"],
        "roleConfigurationId": role["RoleConfigurationId"],
        "roleConfigurationName": role["RoleConfigurationName"],
        "zoneId": token_info["ZoneId"],
        "site": site,
        "authUrl": auth_url,
        "expiresAt": int(time.time()) + 3600 * 12,
    }
    sso.save_credential(cred, sso_info, profile)

    print_message(_("login_success") % sso.cred_path_of_profile(profile))


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
