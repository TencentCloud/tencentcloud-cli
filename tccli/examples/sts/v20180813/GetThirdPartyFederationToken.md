**Example 1: 获取用户临时证书（第三方开发商）**



Input: 

```
tccli sts GetThirdPartyFederationToken --cli-unfold-argument  \
    --UserAccessToken XXXXX \
    --Duration 7200 \
    --ApiAppId XXXXX
```

Output: 
```
{
    "Response": {
        "Credentials": [
            {
                "Token": "xxxxxx",
                "TmpSecretId": "XXXXXX",
                "TmpSecretKey": "XXXXXXX"
            }
        ],
        "ExpiredTime": "7200",
        "RequestId": ""
    }
}
```

