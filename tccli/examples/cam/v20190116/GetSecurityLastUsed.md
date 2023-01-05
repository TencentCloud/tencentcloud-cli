**Example 1: 密钥最后一次访问时间**



Input: 

```
tccli cam GetSecurityLastUsed --cli-unfold-argument  \
    --SecretIdList ***
```

Output: 
```
{
    "Response": {
        "SecretIdLastUsedRows": [
            {
                "SecretId": "***",
                "LastUsedDate": "2022-12-19",
                "LastSecretUsedDate": 1671681023555
            }
        ],
        "RequestId": "b790d4ca-5692-42ae-8a8c-d15c6ed976db"
    }
}
```

