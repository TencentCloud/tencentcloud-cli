**Example 1: 查询账户余额**



Input: 

```
tccli cpdp QueryFlexPlatformAccountBalance --cli-unfold-argument  \
    --IncomeType OCCASION
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "IncomeType": null,
            "Balance": "331300.89",
            "PayableBalance": "331.89",
            "InPayBalance": "448.00",
            "SystemFreezeBalance": "0.00",
            "ManualFreezeBalance": "9.00"
        },
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

