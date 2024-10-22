# coding: utf-8
import random
import string
import sys
import time
import uuid
import webbrowser

from six.moves.urllib.parse import urlencode

from tccli import sso
from tccli.plugins.sso import texts

_AUTH_URL = "https://tencentcloudsso.com/pursue/login"
_CLI_URL = "https://cli.cloud.tencent.com/sso"
_SITE = "cn"
_DEFAULT_LANG = "zh-CN"

_START_SEARCH_PORT = 9000
_END_SEARCH_PORT = _START_SEARCH_PORT + 100


def print_message(msg):
    print(msg)
    sys.stdout.flush()


def login_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = _DEFAULT_LANG
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    login(profile, language)


def login(profile, language):
    characters = string.ascii_letters + string.digits
    state = ''.join(random.choice(characters) for _ in range(32))

    token = _get_token(state, language)

    if token["State"] != state:
        raise ValueError("invalid state %s" % token["state"])

    login_token = token["token"]
    site = token["site"]
    accounts = sso.list_accounts_for_access_assignment(login_token, site)
    print(accounts)
    # todo
    acc = accounts[0]
    roles = sso.list_role_configurations_for_account(acc["Uin"], login_token, site)
    print(roles)

    role = roles[0]
    saml_resp = sso.gen_saml_response(
        login_token, "RoleSAML", acc["Uin"], "", role["RoleConfigurationId"], site)
    print(saml_resp)

    token_info = sso.verify_login_skey(login_token, site)

    role_arn = "qcs::cam::uin/%s:roleName/TencentCloudSSO-%s" % (acc["Uin"], role["RoleConfigurationName"])
    principal_arn = "qcs::cam::uin/%s:saml-provider/TencentReservedSSO-%s" % (acc["Uin"], token_info["ZoneId"])
    cred = sso.assume_role_with_saml(
        saml_resp["SAMLResponse"], principal_arn, role_arn, "ses-%s" % uuid.uuid4(), 7200, site)
    print(cred)

    sso_info = {
        "token": login_token,
        "uin": acc["Uin"],
        "roleConfigurationId": role["RoleConfigurationId"],
        "roleConfigurationName": role["RoleConfigurationName"],
        "zoneId": token_info["ZoneId"],
        "site": site,
    }
    sso.save_credential(cred, sso_info, profile)

    print_message("")


def _get_token(state, language):
    cli_params = {
        "lang": language,
        "site": _SITE,
        "state": state,
        "browser": "no",
    }
    cli_query = urlencode(cli_params)
    cli_url = _CLI_URL + "?" + cli_query
    url_params = {
        "loginType": "tccli",
        "callback": cli_url,
        "state": state,
    }
    url_query = urlencode(url_params)
    auth_url = _AUTH_URL + "?" + url_query

    print_message(texts.get("try_login_with_url"))
    print_message("")
    print_message(auth_url)

    webbrowser.open(auth_url)

    while True:
        time.sleep(1)

        login_state = sso.check_login_state(state)
        if "Error" in login_state:
            raise ValueError(login_state["Error"])

        if login_state["State"] == "NotFound":
            continue

        if login_state["State"] == "Finished":
            return login_state["Token"]

        raise ValueError("invalid resp: %s" % login_state)
