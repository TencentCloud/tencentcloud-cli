**Example 1: 结算中心-冻结资金**



Input: 

```
tccli cpdp FreezeFlexBalance --cli-unfold-argument  \
    --Remark xxx \
    --AmountBeforeTax 0.3 \
    --OutOrderId freeze012 \
    --IncomeType LABOR \
    --OperationType FREEZE \
    --PayeeId 1524013479128928256
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "OrderId": "1524597398137180160"
        },
        "RequestId": "7062a383-4203-4b8e-9e6d-e0eaa9f895ca"
    }
}
```

