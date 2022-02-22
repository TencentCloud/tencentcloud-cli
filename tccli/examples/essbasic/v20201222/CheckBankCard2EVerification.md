**Example 1: 验证银行卡二要素**



Input: 

```
tccli essbasic CheckBankCard2EVerification --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --BankCard 银行卡 \
    --Name 张三
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Result": 102,
        "Description": "银行卡号码有误"
    }
}
```

