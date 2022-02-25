**Example 1: QueryExceedingInfo**



Input: 

```
tccli cpdp QueryExceedingInfo --cli-unfold-argument  \
    --TimeStr 2021-01-01 \
    --PageNumber.Count 10 \
    --PageNumber.Index 0 \
    --Dimension AGENT
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "RequestId": "5073a4f3-44cc-43d1-a6e5-55d750278bbd",
        "Result": {
            "Count": 0,
            "Data": {
                "AgentId": "Agent1",
                "AgentName": "Agent1Name",
                "ExceedingType": "AGENT_EXCEED_100",
                "OrderId": null,
                "AnchorId": null,
                "AnchorName": null
            }
        }
    }
}
```

