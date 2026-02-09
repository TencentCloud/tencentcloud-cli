**Example 1: 同步秘钥**



Input: 

```
tccli cam SyncSecretKey --cli-unfold-argument  \
    --GitSkInfo.0.SecretId AKIDGQOBuT***********HG2f7NQI1ZEi072 \
    --GitSkInfo.0.SecretKey mLkwwj************RSL2WotnV2M4at \
    --GitSkInfo.0.GithubUrl 33
```

Output: 
```
{
    "Response": {
        "SecretStatus": [
            {
                "SecretId": "AKIDGQOBuTr***********G2f7NQI1ZEi072",
                "Status": 1
            }
        ],
        "RequestId": "d8499643-ccca-4abf-80bd-b5417c6f8756"
    }
}
```

