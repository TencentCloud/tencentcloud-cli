# coding: utf-8
import base64
import json
import random
import string
import sys
import time
from six.moves.urllib.parse import urlencode
import webbrowser

from tccli import oauth
from tccli.plugins.auth import texts

_APP_ID = 100038427476
_AUTH_URL = "https://cloud.tencent.com/open/authorize"
_REDIRECT_URL = "https://cli.cloud.tencent.com/oauth"
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

    browser = args.get("browser")

    login(browser != "no", profile, language)


def login(use_browser, profile, language):
    characters = string.ascii_letters + string.digits
    state = ''.join(random.choice(characters) for _ in range(10))

    if use_browser:
        token, cred = _get_token(state, language)
    else:
        token, cred = _get_token_no_browser(state, language)

    if token["state"] != state:
        raise ValueError("invalid state %s" % token["state"])

    oauth.save_credential(token, cred, profile)

    print_message("")
    print_message(texts.get("login_success") % oauth.cred_path_of_profile(profile))


def _get_token(state, language):
    from tccli.plugins.auth import browser_flow

    port, result_queue = browser_flow.try_run(_START_SEARCH_PORT, _END_SEARCH_PORT)

    redirect_params = {
        "redirect_url": "http://localhost:%d" % port,
        "lang": language,
        "site": _SITE,
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
    auth_url = _AUTH_URL + "?" + url_query

    if not webbrowser.open(auth_url):
        print_message(texts.get("login_failed_due_to_no_browser"))
        sys.exit(1)

    print_message(texts.get("login_prompt"))
    print_message(auth_url)

    # use polling to avoid being unresponsive in python2
    while result_queue.empty():
        time.sleep(1)

    result = result_queue.get()
    if isinstance(result, Exception):
        raise result

    return result


def _get_token_no_browser(state, language):
    redirect_params = {
        "browser": "no",
        "lang": language,
        "site": _SITE,
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
    auth_url = _AUTH_URL + "?" + url_query

    print_message(texts.get("login_prompt_no_browser"))
    print_message("")
    print_message(auth_url)

    try:
        input_func = raw_input
    except NameError:
        input_func = input

    user_input = input_func(texts.get("login_prompt_code_no_browser"))
    token = json.loads(base64.b64decode(user_input))
    cred = oauth.get_temp_cred(token["accessToken"], token["site"])
    return token, cred
