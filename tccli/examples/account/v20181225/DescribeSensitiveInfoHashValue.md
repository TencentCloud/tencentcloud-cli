**Example 1: 获取用户敏感信息哈希值**



Input: 

```
tccli account DescribeSensitiveInfoHashValue --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HasSecurePhone": 1,
        "HasAuthInfo": 1,
        "HashAlgorithm": "md5",
        "Salt": "969f9e11",
        "SecurePhoneHashValue": "9c6cdaf0b33bc5cb991b113851d9f426",
        "AuthNameHashValue": "fcbc647244e51c43c129afb13716c40d",
        "RequestId": "95f11eac-1821-4eea-a36f-22bdd31b41f1"
    }
}
```

