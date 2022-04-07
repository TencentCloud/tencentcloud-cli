**Example 1: 创建数据加工任务**



Input: 

```
tccli cls ModifyDataTransform --cli-unfold-argument  \
    --DstResources.0.TopicId xx \
    --DstResources.0.Alias xx \
    --EnableFlag 0 \
    --EtlContent xx \
    --Name xx \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

