# coding: utf-8
import os

from tccli import oauth
from tccli.plugins.auth import texts


def logout_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = "zh-CN"
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    cred_path = oauth.cred_path_of_profile(profile)
    if os.path.exists(cred_path):
        os.remove(cred_path)
    print(texts.get("logout") % cred_path)
