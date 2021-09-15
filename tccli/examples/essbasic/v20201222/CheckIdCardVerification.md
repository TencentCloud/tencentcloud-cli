**Example 1: CheckIdCardVerification**



Input: 

```
tccli essbasic CheckIdCardVerification --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --Name 张三 \
    --IdCardNumber 110101190101011030
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Result": 104,
        "Description": "证件库中无此身份证记录"
    }
}
```

