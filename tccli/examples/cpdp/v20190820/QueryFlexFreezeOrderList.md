**Example 1: 结算中心-查询冻结单列表**



Input: 

```
tccli cpdp QueryFlexFreezeOrderList --cli-unfold-argument  \
    --PageNumber.Count 10 \
    --PageNumber.Index 1 \
    --EndTime 2022-05-12 00:00:00 \
    --PayeeId 字符串 \
    --OperationType 1 \
    --StartTime 2022-05-06 00:00:00
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "List": null,
            "Count": null
        },
        "RequestId": "8eab2787-decd-470d-8d2d-1f5f2e31ecb3"
    }
}
```

