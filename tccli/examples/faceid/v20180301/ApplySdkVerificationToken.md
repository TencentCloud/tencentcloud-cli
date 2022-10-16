**Example 1: 获取Token成功**



Input: 

```
tccli faceid ApplySdkVerificationToken --cli-unfold-argument  \
    --NeedVerifyIdCard True \
    --Extra xx \
    --IdCardType HK
```

Output: 
```
{
    "Response": {
        "SdkToken": "A561B769-C347-4724-A69A-6C3B3483E107",
        "RequestId": "d73c0c05-f7ff-419c-84cb-0756303b1925"
    }
}
```

