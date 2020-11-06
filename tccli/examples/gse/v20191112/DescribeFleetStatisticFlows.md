**Example 1: 查询舰队统计用量**



Input: 

```
tccli gse DescribeFleetStatisticFlows --cli-unfold-argument  \
    --Limit 10 \
    --EndTime 2020-09-22 00:00:00 \
    --FleetId fleet-qp3g3caa-nkeekxw6 \
    --BeginTime 2020-09-22 00:00:00 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "UsedFlowList": [
            {
                "TotalUsedFlowMegaBytes": 1024,
                "BeginTime": "2020-05-13T01:02:03Z"
            }
        ],
        "UsedTimeList": [
            {
                "TotalUsedTimeSeconds": 60,
                "BeginTime": "2020-05-13T01:02:03Z"
            }
        ],
        "TotalCount": 10,
        "TimeType": "DAY",
        "RequestId": "4520ba54-982e-46e2-9a0b-63c963c34fc6"
    }
}
```

