import json
import os
import time
import uuid

import requests

_API_ENDPOINT = "https://cli.cloud.tencent.com"
_CRED_REFRESH_SAFE_DUR = 60 * 5
_SKEY_REFRESH_SAFE_DUR = 3600 * 12 - 300


def maybe_refresh_credential(profile):
    cred_path = cred_path_of_profile(profile)
    try:
        with open(cred_path, "r") as cred_file:
            cred = json.load(cred_file)
    except IOError:
        # file not found, don't check
        return

    if cred.get("type") != "sso":
        return

    try:
        now = time.time()

        expires_at = cred["expiresAt"]
        if expires_at - now > _CRED_REFRESH_SAFE_DUR:
            return

        sso_info = cred["sso"]
        site = sso_info["site"]
        sso_expires = sso_info["expiresAt"]
        if sso_expires - now < _SKEY_REFRESH_SAFE_DUR:
            # sso can't be refreshed if expired, re-login is required
            return

        saml_resp = gen_saml_response(
            sso_info["token"], "RoleSAML", sso_info["uin"], "", sso_info["roleConfigurationId"],
            sso_info["site"]
        )

        role_arn = "qcs::cam::uin/%s:roleName/TencentCloudSSO-%s" % (sso_info["uin"], sso_info["roleConfigurationName"])
        principal_arn = "qcs::cam::uin/%s:saml-provider/TencentReservedSSO-%s" % (sso_info["uin"], sso_info["zoneId"])
        cred = assume_role_with_saml(
            saml_resp["SAMLResponse"], principal_arn, role_arn, "ses-%s" % uuid.uuid4(), 7200, site)
        save_credential(cred, sso_info, profile)

    except KeyError as e:
        print("failed to refresh credential, your credential file(%s) is corrupted, %s" % (cred_path, e))

    except Exception as e:
        print("failed to refresh credential, %s" % e)


def verify_login_skey(token, site):
    api_endpoint = _API_ENDPOINT + "/api/org/verify_login_skey"

    body = {
        "TraceId": str(uuid.uuid4()),
        "Site": site,
        "LoginSkey": token,
    }
    http_response = requests.post(api_endpoint, json=body)
    try:
        resp = http_response.json()
        if "Error" in resp:
            raise ValueError(http_response.content)
        return resp
    except Exception:
        print(http_response.content)
        raise


def list_accounts_for_access_assignment(token, site):
    api_endpoint = _API_ENDPOINT + "/api/org/list_accounts_for_access_assignment"
    page_num = 1
    page_size = 20

    accounts = []
    while True:
        body = {
            "TraceId": str(uuid.uuid4()),
            "Site": site,
            "LoginToken": token,
            "PageNum": page_num,
            "PageSize": page_size,
        }
        http_response = requests.post(api_endpoint, json=body)
        resp = http_response.json()
        if "Error" in resp:
            raise ValueError(http_response.content)

        try:
            accounts.extend(resp.get("Accounts", []))
            if resp["TotalCounts"] <= len(accounts):
                break

            page_num += 1
        except Exception:
            print(http_response.content)
            raise

    return accounts


def list_role_configurations_for_account(uin, token, site):
    api_endpoint = _API_ENDPOINT + "/api/org/list_role_configurations_for_account"
    page_size = 20

    configs = []
    next_token = ""
    while True:
        body = {
            "TraceId": str(uuid.uuid4()),
            "Site": site,
            "TargetUin": uin,
            "LoginToken": token,
            "MaxResults": page_size,
            "NextToken": next_token,
        }
        http_response = requests.post(api_endpoint, json=body)
        try:
            resp = http_response.json()

            if "Error" in resp:
                raise ValueError(http_response.content)

            configs.extend(resp.get("RoleConfigurationsForAccount", []))
            if not resp["IsTruncated"]:
                break

            next_token = resp["NextToken"]
        except Exception:
            print(http_response.content)
            raise

    return configs


def gen_saml_response(token, login_type, uin, user_id, conf_id, site):
    api_endpoint = _API_ENDPOINT + "/api/org/gen_saml_response"

    body = {
        "TraceId": str(uuid.uuid4()),
        "Site": site,
        "LoginToken": token,
        "LoginType": login_type,
        "TargetUin": uin,
        "UserId": user_id,
        "RoleConfigurationId": conf_id,
    }
    http_response = requests.post(api_endpoint, json=body)
    try:
        resp = http_response.json()
        if "Error" in resp:
            raise ValueError(http_response.content)

        return resp
    except Exception:
        print(http_response.content)
        raise


def assume_role_with_saml(saml_assertion, principal_arn, role_arn, role_ses_name, dur, site):
    api_endpoint = _API_ENDPOINT + "/api/sts/assume_role_with_saml"

    body = {
        "TraceId": str(uuid.uuid4()),
        "Site": site,
        "SAMLAssertion": saml_assertion,
        "PrincipalArn": principal_arn,
        "RoleArn": role_arn,
        "RoleSessionName": role_ses_name,
        "DurationSeconds": dur,
    }
    http_response = requests.post(api_endpoint, json=body)
    try:
        resp = http_response.json()
        if "Error" in resp:
            raise ValueError(http_response.content)
        return resp
    except Exception:
        print(http_response.content)
        raise


def save_credential(cred, sso_info, profile):
    cred_path = cred_path_of_profile(profile)

    cred = {
        "type": "sso",
        "secretId": cred["Credentials"]["TmpSecretId"],
        "secretKey": cred["Credentials"]["TmpSecretKey"],
        "token": cred["Credentials"]["Token"],
        "expiresAt": cred["ExpiredTime"],
        "sso": {
            "token": sso_info["token"],
            "uin": sso_info["uin"],
            "roleConfigurationId": sso_info["roleConfigurationId"],
            "roleConfigurationName": sso_info["roleConfigurationName"],
            "zoneId": sso_info["zoneId"],
            "site": sso_info["site"],
            "authUrl": sso_info["authUrl"],
            "expiresAt": sso_info["expiresAt"],
        },
    }
    with open(cred_path, "w") as cred_file:
        json.dump(cred, cred_file, indent=4)


def cred_path_of_profile(profile):
    return os.path.join(os.path.expanduser("~"), ".tccli", profile + ".credential")


def check_login_state(state):
    api_endpoint = _API_ENDPOINT + "/api/sso/check_login_state"

    body = {
        "TraceId": str(uuid.uuid4()),
        "State": state,
    }
    http_response = requests.post(api_endpoint, json=body)
    try:
        return http_response.json()
    except Exception:
        print(http_response.content)
        raise
