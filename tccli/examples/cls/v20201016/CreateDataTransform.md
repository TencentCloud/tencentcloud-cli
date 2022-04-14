**Example 1: 创建数据加工任务**



Input: 

```
tccli cls CreateDataTransform --cli-unfold-argument  \
    --EnableFlag 1 \
    --Name xx \
    --FuncType 0 \
    --PreviewLogStatistics.0.LineNum 0 \
    --PreviewLogStatistics.0.FailReason errorcode \
    --PreviewLogStatistics.0.DstTopicId 81XXXXe5-e39e-4a1e-b2d4-a778df97d825 \
    --PreviewLogStatistics.0.LogContent XXXX \
    --PreviewLogStatistics.0.Time 2017-08-08 12:12:12 \
    --SrcTopicId xx \
    --TaskType 0 \
    --DstResources.0.TopicId 3d9bXXXX-05a4-4435-ac65-f43e684329b3 \
    --DstResources.0.Alias 别名 \
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

