**Example 1: 电子签企业版-合同催办接口**



Input: 

```
tccli ess CreateFlowReminds --cli-unfold-argument  \
    --Operator.UserId xxx \
    --FlowIds xxx
```

Output: 
```
{
    "Response": {
        "RemindFlowRecords": [
            {
                "CanRemind": true,
                "FlowId": "xxx",
                "RemindMessage": "签署人 xxx: 此签署人已催办过；"
            }
        ],
        "RequestId": "s1675154686215203499"
    }
}
```

