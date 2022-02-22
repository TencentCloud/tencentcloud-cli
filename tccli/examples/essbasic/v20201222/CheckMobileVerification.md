**Example 1: 验证手机号三要素**



Input: 

```
tccli essbasic CheckMobileVerification --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --Mobile 14000000000 \
    --Name 张三 \
    --IdCardNumber 110101190101011030
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Result": 101,
        "Description": "查无记录"
    }
}
```

