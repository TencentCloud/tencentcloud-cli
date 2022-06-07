**Example 1: 收款用户账户列表查询**



Input: 

```
tccli cpdp QueryFlexPayeeAccountList --cli-unfold-argument  \
    --PageNumber.Count 10 \
    --PageNumber.Index 1 \
    --EndTime 2022-05-12 00:00:00 \
    --StartTime 2022-05-06 00:00:00 \
    --PropertyInfo.SettleRightStatus ENABLE \
    --PropertyInfo.PaymentRightStatus ENABLE
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "List": [],
            "Count": 0
        },
        "RequestId": "38d7b2b1-4c14-4a04-81d4-889267bad6db"
    }
}
```

