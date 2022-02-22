**Example 1: 检测人脸核身结果**



Input: 

```
tccli essbasic CheckFaceIdentify --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId 参与人脸核身用户的UserId \
    --VerifyChannel FACEID \
    --VerifyResult WbAppIdOrderNumber \
    --Name 张三 \
    --IdCardNumber 110101190101011030
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Result": 0,
        "Description": "",
        "ChannelName": "腾讯电子签慧眼",
        "VerifiedOn": 1609901339,
        "SerialNumber": "流水号",
        "VerifyServerIp": "1.2.3.4",
        "PhotoFileName": "",
        "PhotoFileData": ""
    }
}
```

