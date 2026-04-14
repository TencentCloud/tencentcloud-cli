import json
import os

from tccli import oauth, sso


def maybe_refresh_credential(profile):
    try:
        with open(cred_path_of_profile(profile), "r") as cred_file:
            cred = json.load(cred_file)
    except IOError:
        # file not found, don't check
        return

    if cred.get("type", "") == "oauth":
        oauth.maybe_refresh_credential(profile)
        return

    if cred.get("type", "") == "sso":
        sso.maybe_refresh_credential(profile)
        return


def cred_path_of_profile(profile):
    return os.path.join(os.path.expanduser("~"), ".tccli", profile + ".credential")
