import json
import os
import time

import requests
import uuid

_API_ENDPOINT = "https://cli.cloud.tencent.com"
_CRED_REFRESH_SAFE_DUR = 60 * 5
_ACCESS_REFRESH_SAFE_DUR = 60 * 5


def maybe_refresh_credential(profile):
    cred_path = cred_path_of_profile(profile)
    try:
        with open(cred_path, "r") as cred_file:
            cred = json.load(cred_file)
    except IOError:
        # file not found, don't check
        return

    if cred.get("type") != "oauth":
        return

    try:
        now = time.time()

        expires_at = cred["expiresAt"]
        if expires_at - now > _CRED_REFRESH_SAFE_DUR:
            return

        token_info = cred["oauth"]
        site = token_info["site"]
        access_expires = token_info["expiresAt"]
        if access_expires - now < _ACCESS_REFRESH_SAFE_DUR:
            refresh_token = token_info["refreshToken"]
            open_id = token_info["openId"]
            new_token = refresh_user_token(refresh_token, open_id, site)
            token_info.update(new_token)

        access_token = token_info["accessToken"]
        new_cred = get_temp_cred(access_token, site)
        save_credential(token_info, new_cred, profile)

    except KeyError as e:
        print("failed to refresh credential, your credential file(%s) is corrupted, %s" % (cred_path, e))

    except Exception as e:
        print("failed to refresh credential, %s" % e)


def refresh_user_token(ref_token, open_id, site):
    api_endpoint = _API_ENDPOINT + "/refresh_user_token"
    body = {
        "TraceId": str(uuid.uuid4()),
        "RefreshToken": ref_token,
        "OpenId": open_id,
        "Site": site,
    }
    http_response = requests.post(api_endpoint, json=body, verify=False)
    resp = http_response.json()

    if "Error" in resp:
        raise ValueError("refresh_user_token: %s" % json.dumps(resp))

    return {
        "accessToken": resp["AccessToken"],
        "expiresAt": resp["ExpiresAt"],
    }


def get_temp_cred(access_token, site):
    api_endpoint = _API_ENDPOINT + "/get_temp_cred"
    body = {
        "TraceId": str(uuid.uuid4()),
        "AccessToken": access_token,
        "Site": site,
    }
    http_response = requests.post(api_endpoint, json=body, verify=False)
    resp = http_response.json()

    if "Error" in resp:
        raise ValueError("get_temp_key: %s" % json.dumps(resp))

    return {
        "secretId": resp["SecretId"],
        "secretKey": resp["SecretKey"],
        "token": resp["Token"],
        "expiresAt": resp["ExpiresAt"],
    }


def cred_path_of_profile(profile):
    return os.path.join(os.path.expanduser("~"), ".tccli", profile + ".credential")


def save_credential(token, new_cred, profile):
    cred_path = cred_path_of_profile(profile)

    cred = {
        "type": "oauth",
        "secretId": new_cred["secretId"],
        "secretKey": new_cred["secretKey"],
        "token": new_cred["token"],
        "expiresAt": new_cred["expiresAt"],
        "oauth": {
            "openId": token["openId"],
            "accessToken": token["accessToken"],
            "expiresAt": token["expiresAt"],
            "refreshToken": token["refreshToken"],
            "site": token["site"],
        },
    }
    with open(cred_path, "w") as cred_file:
        json.dump(cred, cred_file, indent=4)
