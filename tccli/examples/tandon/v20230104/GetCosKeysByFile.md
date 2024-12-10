**Example 1: success**

获取成功

Input: 

```
tccli tandon GetCosKeysByFile --cli-unfold-argument  \
    --FilePath 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Bucket": "1",
            "Credentials": {
                "SessionToken": "1",
                "TmpSecretId": "2",
                "TmpSecretKey": "3"
            },
            "ExpiredTime": 1731500616,
            "Prefix": "1",
            "Region": "1"
        },
        "RequestId": "123"
    }
}
```

