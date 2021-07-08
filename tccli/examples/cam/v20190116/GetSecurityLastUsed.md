**Example 1: 获取密钥最近使用情况**



Input: 

```
tccli cam GetSecurityLastUsed --cli-unfold-argument  \
    --SecretIdList xxxxxxxxx
```

Output: 
```
{
    "Response": {
        "SecretIdLastUsedRows": [
            {
                "SecretId": "xxxxxxxxx",
                "LastUsedDate": "2021-03-20"
            }
        ],
        "RequestId": "15a763ee-c2da-446a-9b21-25632d7cecb5"
    }
}
```

