**Example 1: 认证通过示例**



Input: 

```
tccli faceid EncryptedPhoneVerification --cli-unfold-argument  \
    --IdCard 21b2ad431ee1f6d32c3f54c23c684751 \
    --Name 615db57aa314529aaa0fbe95b3e95bd3 \
    --Phone 18c6f9a0ca21c6bc9c58675adfc4196e \
    --EncryptionMode 1
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

