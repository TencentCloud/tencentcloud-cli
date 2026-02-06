**Example 1: 创建重建索引任务**



Input: 

```
tccli cls CreateRebuildIndexTask --cli-unfold-argument  \
    --TopicId a5ce0c9c-xxxx-44a5-bc79-5f2190626bd0 \
    --StartTime 1234567890123 \
    --EndTime 1234567890456
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "TaskId": "6ef60bec-0242-43af-bb20-270359fb54ax"
    }
}
```

