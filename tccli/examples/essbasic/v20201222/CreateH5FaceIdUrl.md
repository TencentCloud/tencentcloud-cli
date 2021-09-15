**Example 1: 获取慧眼H5人脸核身Url**



Input: 

```
tccli essbasic CreateH5FaceIdUrl --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId 要人脸核身用户的UserId \
    --WbAppId 分配的慧眼H5业务ID \
    --Name 姓名 \
    --IdCardType ID_CARD \
    --IdCardNumber 110101190101011030
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Url": "https://ess.tencent.com/abcd"
    }
}
```

