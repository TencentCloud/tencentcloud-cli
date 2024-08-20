# coding: utf-8
import texts


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
    print("login")


def login_no_browser():
    print(texts.get("login_prompt"))
