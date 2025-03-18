**Example 1: 查询自治事件任务列表**



Input: 

```
tccli dbbrain DescribeDBAutonomyActions --cli-unfold-argument  \
    --EventId 37 \
    --InstanceId crs-1p8z8saa \
    --Product redis
```

Output: 
```
{
    "Response": {
        "Actions": [
            {
                "ActionId": 422,
                "CreateTime": "2025-03-14 11:50:00",
                "EventId": 37,
                "ExpireTime": 0,
                "FinishTime": "2025-03-14 11:50:00",
                "Reason": "指标\"mem_util\"大于50%持续超过15分钟",
                "Status": "TERMINATED",
                "TriggerTime": "2025-03-14 11:50:00",
                "Type": "RedisAutoScaleUp",
                "UpdateTime": "2025-03-14 11:50:00"
            },
            {
                "ActionId": 421,
                "CreateTime": "2025-03-14 11:35:00",
                "EventId": 37,
                "ExpireTime": 0,
                "FinishTime": "2025-03-14 11:35:00",
                "Reason": "指标\"mem_util\"大于50%持续超过15分钟",
                "Status": "TERMINATED",
                "TriggerTime": "2025-03-14 11:35:00",
                "Type": "RedisAutoScaleUp",
                "UpdateTime": "2025-03-14 11:35:00"
            },
            {
                "ActionId": 420,
                "CreateTime": "2025-03-14 11:16:00",
                "EventId": 37,
                "ExpireTime": 0,
                "FinishTime": "2025-03-14 11:20:00",
                "Reason": "指标\"mem_util\"大于50%持续超过15分钟",
                "Status": "CANCELLED",
                "TriggerTime": "2025-03-14 11:16:00",
                "Type": "RedisAutoScaleUp",
                "UpdateTime": "2025-03-14 11:16:00"
            },
            {
                "ActionId": 419,
                "CreateTime": "2025-03-14 11:01:00",
                "EventId": 37,
                "ExpireTime": 0,
                "FinishTime": "2025-03-14 11:01:00",
                "Reason": "指标\"mem_util\"大于50%持续超过15分钟",
                "Status": "TERMINATED",
                "TriggerTime": "2025-03-14 11:01:00",
                "Type": "RedisAutoScaleUp",
                "UpdateTime": "2025-03-14 11:01:00"
            },
            {
                "ActionId": 418,
                "CreateTime": "2025-03-14 10:46:00",
                "EventId": 37,
                "ExpireTime": 0,
                "FinishTime": "2025-03-14 10:46:00",
                "Reason": "指标\"mem_util\"大于50%持续超过15分钟",
                "Status": "TERMINATED",
                "TriggerTime": "2025-03-14 10:46:00",
                "Type": "RedisAutoScaleUp",
                "UpdateTime": "2025-03-14 10:46:00"
            }
        ],
        "RequestId": "6ae91539-89e6-4b80-be25-cfc3cd2714f3",
        "TotalCount": 5
    }
}
```

