import json

import requests
import uuid

_API_ENDPOINT = "https://cli.cloud.tencent.com"


def refresh_token(ref_token, open_id):
    api_endpoint = _API_ENDPOINT + "/refresh_token"
    body = {
        "TraceId": str(uuid.uuid4()),
        "RefreshToken": ref_token,
        "OpenId": open_id,
    }
    http_response = requests.post(api_endpoint, json=body, verify=False)
    resp = http_response.json()

    if "Error" in resp:
        raise ValueError(json.dumps(resp))

    return {
        "access_token": resp["AccessToken"],
        "expires_at": resp["ExpiresAt"],
    }


def get_temp_key(access_token):
    api_endpoint = _API_ENDPOINT + "/get_temp_key"
    body = {
        "TraceId": str(uuid.uuid4()),
        "AccessToken": access_token,
    }
    http_response = requests.post(api_endpoint, json=body, verify=False)
    resp = http_response.json()

    if "Error" in resp:
        raise ValueError(json.dumps(resp))

    return {
        "secret_id": resp["SecretId"],
        "secret_key": resp["SecretKey"],
        "token": resp["Token"],
        "expires_at": resp["ExpiresAt"],
    }
