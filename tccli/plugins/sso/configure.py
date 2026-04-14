# coding: utf-8
import json
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from tccli import sso
from tccli.plugins.sso import texts, configs


def configure_command_entrypoint(args, parsed_globals):
    language = parsed_globals.get("language")
    if not language:
        language = configs.DEFAULT_LANG
    texts.set_lang(language)

    profile = parsed_globals.get("profile", "default")
    if not profile:
        profile = "default"

    cred_data = {}
    try:
        with open(sso.cred_path_of_profile(profile), "r") as cred_file:
            cred_data = json.load(cred_file)
    except IOError:
        pass

    if "sso" not in cred_data:
        cred_data["sso"] = {}

    auth_url = args.get("url")
    if not auth_url.startswith("http://") and not auth_url.startswith("https://"):
        auth_url = "https://" + auth_url

    parsed_url = urlparse(auth_url)
    if not (parsed_url.scheme in ("http", "https") and parsed_url.netloc):
        print(texts.get("invalid_auth_url") % auth_url)
        return

    cred_data["sso"]["authUrl"] = auth_url
    with open(sso.cred_path_of_profile(profile), "w") as cred_file:
        json.dump(cred_data, cred_file, indent=4)

    print(texts.get("configure_succeed") % auth_url)
