**Example 1: 测试**



Input: 

```
tccli dlc UpdateApiKeyStatus --cli-unfold-argument  \
    --ApiKeyId apikey-migrated-00000003 \
    --Status Revoked
```

Output: 
```
{
    "Response": {
        "ApiKey": "sk-proj-xYd65Mh550ZBcQU7c91RnrfPseoZmyBsTSDfCPFErPa3iQhb",
        "ApiKeyId": "apikey-migrated-00000003",
        "AppId": 260200066,
        "CreateTime": 1779813850814,
        "Name": "sigma-token-1234",
        "ServiceId": "svc-migrated-00000022",
        "ServiceName": "xgboost-hhhh",
        "Status": "Revoked",
        "SubAccountUin": "700002655694",
        "Uin": "700002655694",
        "UpdateTime": 1780747856084,
        "RequestId": "9294f5c7-aa98-4446-9b3d-745b7cfc83fa"
    }
}
```

