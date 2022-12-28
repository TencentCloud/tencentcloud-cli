**Example 1: 查询服务商账户余额**



Input: 

```
tccli cpdp QueryFlexServiceProviderAccountBalance --cli-unfold-argument  \
    --ServiceProviderId CM61695xxx1840
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "Balance": "1.99"
        },
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

