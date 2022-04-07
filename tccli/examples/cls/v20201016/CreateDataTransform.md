**Example 1: 创建数据加工任务**



Input: 

```
tccli cls CreateDataTransform --cli-unfold-argument  \
    --EnableFlag 1 \
    --Name xx \
    --FuncType 0 \
    --PreviewLogStatistics.0.LineNum 0 \
    --PreviewLogStatistics.0.FailReason xx \
    --PreviewLogStatistics.0.DstTopicId xx \
    --PreviewLogStatistics.0.LogContent xx \
    --PreviewLogStatistics.0.Time xx \
    --SrcTopicId xx \
    --TaskType 0 \
    --DstResources.0.TopicId xx \
    --DstResources.0.Alias xx \
    --EtlContent xx
```

Output: 
```
{
    "Response": {
        "TaskId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

