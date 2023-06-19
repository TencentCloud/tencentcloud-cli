**Example 1: 获取联合身份临时证书**

获取联合身份临时证书

Input: 

```
tccli sts GetFederationTokenForHighConcurrency --cli-unfold-argument  \
    --Name 123 \
    --Policy %7B%22version%22%3A%222.0%22%2C%22statement%22%3A%5B%7B%22effect%22%3A%22deny%22%2C%22action%22%3A%22*%22%2C%22resource%22%3A%22*%22%7D%5D%7D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "TmpSecretId": "AKID***l-t9oz",
            "TmpSecretKey": "pvfd***cMzjsY=",
            "Token": "KXZV***Dih2azlSQ"
        },
        "Expiration": "2023-06-14T05:06:57Z",
        "ExpiredTime": 1686719217,
        "RequestId": "db80656b-dcda-4d8f-971f-0dfa3ab88b1b"
    }
}
```

