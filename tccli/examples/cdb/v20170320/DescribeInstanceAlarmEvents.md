**Example 1: 查询实例事件信息**



Input: 

```
tccli cdb DescribeInstanceAlarmEvents --cli-unfold-argument  \
    --InstanceId cdb-5939glez \
    --EventName Switch \
    --EventStatus 1 \
    --StartTime 2024-01-15 00:00:00 \
    --EndTime 2024-01-30 00:00:00 \
    --Order DESC \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "EventName": "Switch",
                "EventStatus": "1",
                "OccurTime": "2024-01-21 06:10:59"
            },
            {
                "EventName": "Switch",
                "EventStatus": "0",
                "OccurTime": "2024-01-15 21:57:49"
            },
            {
                "EventName": "Switch",
                "EventStatus": "1",
                "OccurTime": "2024-01-15 21:57:45"
            }
        ],
        "RequestId": "mnksadas-cb0d-4943-9b17-c3306ed3d",
        "TotalCount": 3
    }
}
```

