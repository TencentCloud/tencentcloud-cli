# coding: utf-8
import base64
import json
import random
import string
import sys
from urllib import urlencode

import texts
import webbrowser

from tccli import oauth

_APP_ID = 700001249938
_REDIRECT_URL = "https://cli.cloud.tencent.com/oauth"

_START_SEARCH_PORT = 9000
_END_SEARCH_PORT = _START_SEARCH_PORT + 100


def login_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = "zh-CN"
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    browser = args.get("browser")

    login(browser != "no", profile)


def login(use_browser, profile):
    characters = string.ascii_letters + string.digits
    state = ''.join(random.choice(characters) for _ in range(10))

    if use_browser:
        token = _get_token(state)
    else:
        token = _get_token_no_browser(state)

    if token["state"] != state:
        raise ValueError("invalid state %s" % token["state"])

    cred = oauth.get_temp_cred(token["accessToken"])
    oauth.save_credential(token, cred, profile)

    print("")
    print(texts.get("cred_has_been_written_to") % oauth.cred_path_of_profile(profile))


def _get_token(state):
    import browser_flow

    port, result_queue = browser_flow.try_run(_START_SEARCH_PORT, _END_SEARCH_PORT)

    redirect_params = {
        "redirect_url": "http://localhost:%d" % port,
    }
    redirect_query = urlencode(redirect_params)
    redirect_url = _REDIRECT_URL + "?" + redirect_query
    url_params = {
        "scope": "login",
        "app_id": _APP_ID,
        "redirect_url": redirect_url,
        "state": state,
    }
    url_query = urlencode(url_params)
    auth_url = "https://cloud.tencent.com/open/authorize?" + url_query

    if not webbrowser.open(auth_url):
        print(texts.get("login_failed_due_to_no_browser"))
        sys.exit(1)

    print(texts.get("login_prompt"))
    print(auth_url)

    result = result_queue.get()
    if isinstance(result, Exception):
        raise result

    return result


def _get_token_no_browser(state):
    redirect_params = {
        "browser": "no",
    }
    redirect_query = urlencode(redirect_params)
    redirect_url = _REDIRECT_URL + "?" + redirect_query
    url_params = {
        "scope": "login",
        "app_id": _APP_ID,
        "redirect_url": redirect_url,
        "state": state,
    }
    url_query = urlencode(url_params)
    auth_url = "https://cloud.tencent.com/open/authorize?" + url_query

    print(texts.get("login_prompt_no_browser"))
    print("")
    print(auth_url)

    try:
        input_func = raw_input
    except NameError:
        input_func = input

    user_input = input_func(texts.get("login_prompt_code_no_browser"))
    return json.loads(base64.b64decode(user_input))
