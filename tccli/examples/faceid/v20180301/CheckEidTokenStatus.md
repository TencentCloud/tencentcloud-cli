**Example 1: 获取E证通Token状态成功示例**



Input: 

```
tccli faceid CheckEidTokenStatus --cli-unfold-argument  \
    --EidToken 2B3B265E-2C91-5A62-B32D-D0CA5C3F1A15
```

Output: 
```
{
    "Response": {
        "RequestId": "dd4e965c-5a6f-43ee-7764-8272e16b85a3",
        "Status": "doing"
    }
}
```

**Example 2: 获取E政通Token状态失败示例**



Input: 

```
tccli faceid CheckEidTokenStatus --cli-unfold-argument  \
    --EidToken 3B3B265E-3C91-5A62-B32D-D0CA5C3F1A15
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.BizTokenIllegal",
            "Message": "BizToken不合法。"
        },
        "RequestId": "9ad38b82-7b5c-4bb1-b6c0-44ce86bc148e"
    }
}
```

