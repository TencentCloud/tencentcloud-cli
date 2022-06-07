**Example 1: 结算中心-查询结算单**



Input: 

```
tccli cpdp QueryFlexSettlementOrderList --cli-unfold-argument  \
    --PageNumber.Count 10 \
    --PageNumber.Index 1 \
    --EndTime 2022-05-12 00:00:00 \
    --PayeeId 1524013479128928256 \
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
        "RequestId": "66a06170-e747-41ec-b6cc-ff81bd7f43f3"
    }
}
```

