# coding: utf-8
import sys

import texts
import webbrowser

_app_id = 700001249938
_redirect_url = "https://cli.cloud.tencent.com/oauth"


def login_command_entrypoint(args, parsed_globals):
    print(args)

    language = parsed_globals.get("language", "zh-CN")
    texts.set_lang(language)

    no_browser = args.get("no-browser", False)

    if no_browser:
        login_no_browser()
    else:
        login()


def login():
    state = "qwer"
    entrypoint_url = "https://https://cloud.tencent.com/open/authorize?scope=login&app_id=%s&redirect_url=%s&state=%s" % (
        _app_id, _redirect_url, state)
    if not webbrowser.open(entrypoint_url):
        print(texts.get("login_failed_no_browser"))
        sys.exit(1)


def login_no_browser():
    print(texts.get("login_prompt"))
