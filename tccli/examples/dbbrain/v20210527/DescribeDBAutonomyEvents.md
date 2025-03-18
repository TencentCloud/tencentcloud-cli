**Example 1: 查询自治事件列表**



Input: 

```
tccli dbbrain DescribeDBAutonomyEvents --cli-unfold-argument  \
    --Product redis \
    --InstanceId crs-1p8z8saa \
    --StartTime 2025-03-13T11:11:37+08:00 \
    --EndTime 2025-03-14T11:11:37+08:00
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "CreateTime": 1741920360000,
                "EventId": 37,
                "FinishTime": 172800000,
                "LastTriggerTime": 1741924080000,
                "Reason": "内存利用率过高",
                "Status": "RUNNING",
                "TriggerTime": 1741919460000,
                "Type": "RedisAutoScale",
                "UpdateTime": 1741924080000
            },
            {
                "CreateTime": 1741869480000,
                "EventId": 36,
                "FinishTime": 1741919334000,
                "LastTriggerTime": 1741919280000,
                "Reason": "内存利用率过高",
                "Status": "TERMINATED",
                "TriggerTime": 1741868880000,
                "Type": "RedisAutoScale",
                "UpdateTime": 1741919334000
            },
            {
                "CreateTime": 1741868460000,
                "EventId": 35,
                "FinishTime": 1741868520000,
                "LastTriggerTime": 1741868460000,
                "Reason": "内存利用率过高",
                "Status": "FINISHED",
                "TriggerTime": 1741867860000,
                "Type": "RedisAutoScale",
                "UpdateTime": 1741868520000
            }
        ],
        "RequestId": "ef7c643f-7644-4962-9449-b17c6ef6f7c5",
        "TotalCount": 3
    }
}
```

