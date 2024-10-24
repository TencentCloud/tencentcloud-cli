# coding: utf-8
import os

from tccli import sso
from tccli.plugins.sso import texts, configs


def logout_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = configs.DEFAULT_LANG
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    cred_path = sso.cred_path_of_profile(profile)
    if os.path.exists(cred_path):
        os.remove(cred_path)
    print(texts.get("logout_success") % cred_path)
