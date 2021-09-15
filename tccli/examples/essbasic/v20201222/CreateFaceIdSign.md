**Example 1: 生成慧眼API签名**



Input: 

```
tccli essbasic CreateFaceIdSign --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --Values WbAppId Version ...
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Sign": "abcdef1234567890abcdef1234567890"
    }
}
```

