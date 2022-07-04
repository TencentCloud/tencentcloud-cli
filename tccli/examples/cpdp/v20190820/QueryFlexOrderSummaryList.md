**Example 1: 结算单汇总信息列表查询**



Input: 

```
tccli cpdp QueryFlexOrderSummaryList --cli-unfold-argument  \
    --PageNumber.Count 10 \
    --PageNumber.Index 1 \
    --PayeeId xxx \
    --SummaryDate 2022-05-06 \
    --OrderType FREEZE
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
        "RequestId": "38d7b2b1-4c14-4a04-81d4-889267bad611"
    }
}
```

