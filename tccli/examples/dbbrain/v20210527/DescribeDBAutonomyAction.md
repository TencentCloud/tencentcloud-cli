**Example 1: 查询自治事件任务详情**



Input: 

```
tccli dbbrain DescribeDBAutonomyAction --cli-unfold-argument  \
    --ActionId 11 \
    --InstanceId crs-m5toyq2w \
    --Product redis
```

Output: 
```
{
    "Response": {
        "ActionId": 1295,
        "CreateTime": "2025-05-08 14:33:00",
        "EventId": 55,
        "ExpireTime": 0,
        "FinishTime": "2025-05-08 14:50:55",
        "Info": "[{\"DataType\":\"title\",\"Data\":{\"Name\":\"扩容任务【7477146】\"}},{\"Layout\":\"vertical\",\"DataType\":\"table\",\"Data\":{\"Names\":[\"任务类型\"],\"Data\":[{\"预期扩容后规格\":\"4GiB\"}]}},{\"DataType\":\"title\",\"Data\":{\"Name\":\"触1发原因\"}}]",
        "Reason": "指标\\\"mem_util\\\"大于50%持续超过10分钟",
        "RequestId": "80340cd2-adca-4e6a-81af-1ca998426a61",
        "Status": "CANCELLED",
        "TaskId": 7477145,
        "TriggerTime": "2025-05-08 14:33:00",
        "Type": "RedisAutoScaleUp",
        "UpdateTime": "2025-05-08 14:33:00"
    }
}
```

