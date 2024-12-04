**Example 1: 查询实例事件信息**



Input: 

```
tccli cdb DescribeInstanceAlarmEvents --cli-unfold-argument  \
    --InstanceId cdb-fbd5agyt \
    --StartTime 2024-11-15 00:00:00 \
    --EndTime 2024-12-15 00:00:00 \
    --EventName PlannedSwitch \
    --EventStatus - \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "EventName": "PlannedSwitch",
                "EventStatus": "-",
                "InstanceId": "cdb-fbd5agyt",
                "NodeId": "",
                "OccurTime": "2024-11-25 14:46:42"
            }
        ],
        "RequestId": "971e2860-c55b-4323-a831-0001",
        "TotalCount": 1
    }
}
```

