**Example 1: 创建数据加工任务**

数据加工提供对日志数据的过滤、清洗、脱敏、富化、分发等能力,可对标开源组件 Logstash。使用数据加工DSL（Domain Specified Language ）函数，底层基于 Flink 实现，您可轻松处理日志流数据。


Input: 

```
tccli cls CreateDataTransform --cli-unfold-argument  \
    --EnableFlag 1 \
    --Name 数据加工任务 \
    --FuncType 0 \
    --PreviewLogStatistics.0.LineNum 0 \
    --PreviewLogStatistics.0.FailReason errorcode \
    --PreviewLogStatistics.0.DstTopicId 81XXXXe5-e39e-4a1e-b2d4-a778df97d825 \
    --PreviewLogStatistics.0.LogContent XXXX \
    --PreviewLogStatistics.0.Time 2017-08-08 12:12:12 \
    --SrcTopicId xxxx-xx-xx-xx-xxxxxxxx \
    --TaskType 0 \
    --DstResources.0.TopicId 3d9bXXXX-05a4-4435-ac65-f43e684329b3 \
    --DstResources.0.Alias 别名 \
    --EtlContent xx-xx
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

