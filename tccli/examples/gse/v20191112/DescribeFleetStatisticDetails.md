**Example 1: 查询舰队统计详情信息**



Input: 

```
tccli gse DescribeFleetStatisticDetails --cli-unfold-argument  \
    --EndTime 2020-09-22 00:00:00 \
    --FleetId fleet-qp3g3caa-nkeekxw6 \
    --BeginTime 2020-09-22 00:00:00
```

Output: 
```
{
    "Response": {
        "DetailList": [
            {
                "FleetId": "fleet-qp3g3caa-nkeekxw6",
                "InstanceId": "ins-abd1122",
                "InstanceIP": "1.1.1.2",
                "TotalUsedTimeSeconds": 60,
                "TotalUsedFlowMegaBytes": 1024,
                "BeginTime": "2020-05-13T01:00:00Z",
                "EndTime": "2020-05-13T02:00:00Z"
            }
        ],
        "TotalCount": 10,
        "TimeType": "DAY",
        "RequestId": "4520ba54-982e-46e2-9a0b-63c963c34fc6"
    }
}
```

