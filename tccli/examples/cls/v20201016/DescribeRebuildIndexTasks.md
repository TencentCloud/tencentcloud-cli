**Example 1: 获取索引重建任务列表**



Input: 

```
tccli cls DescribeRebuildIndexTasks --cli-unfold-argument  \
    --TopicId 826f8b26-b054-4a0d-xxxx-f3d609f5e0ea
```

Output: 
```
{
    "Response": {
        "RebuildTasks": [
            {
                "TaskId": "02f3e53d-d120-477e-xxxx-cbed37247d97",
                "Status": 0,
                "StatusMessage": "",
                "StartTime": 1234567890123,
                "EndTime": 1234567890234,
                "RemainTime": 1000,
                "CreateTime": 1234567890111,
                "UpdateTime": 0,
                "Progress": 0.0
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

