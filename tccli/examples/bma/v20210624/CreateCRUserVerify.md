**Example 1: 个人认证接口**



Input: 

```
tccli bma CreateCRUserVerify --cli-unfold-argument  \
    --UserName xxx \
    --UserID xxx \
    --UserPhone xxx \
    --VerificationCode xxx
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Note": "xxx",
        "RequestId": "xxx"
    }
}
```

