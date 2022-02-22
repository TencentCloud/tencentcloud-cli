**Example 1: 创建个人帐号**



Input: 

```
tccli essbasic VerifyUser --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --UserId CreateUser生成的UserId
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "UserId": "abcdef1234567890abcdef1234567890"
    }
}
```

