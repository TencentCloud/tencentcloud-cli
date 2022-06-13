**Example 1: 结算**



Input: 

```
tccli cpdp ApplyFlexSettlement --cli-unfold-argument  \
    --OutOrderId 3022050500029 \
    --Remark 字符串 \
    --IncomeType LABOR \
    --PayeeId 1524640861699108864 \
    --AmountBeforeTax 1
```

Output: 
```
{
    "Response": {
        "ErrCode": "SETTLEMENT.ADAPTER_ACCOUNT_SYSTEM_ERROR",
        "ErrMessage": "账户未开立",
        "Result": null,
        "RequestId": "e6161e57-b348-4bd8-a581-c1946c9c34a0"
    }
}
```

