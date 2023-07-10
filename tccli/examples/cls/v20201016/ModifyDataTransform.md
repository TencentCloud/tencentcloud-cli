**Example 1: 修改数据加工任务**

数据加工提供对日志数据的过滤、清洗、脱敏、富化、分发等能力,可对标开源组件 Logstash。使用数据加工DSL（Domain Specified Language ）函数，底层基于 Flink 实现，您可轻松处理日志流数据。


Input: 

```
tccli cls ModifyDataTransform --cli-unfold-argument  \
    --DstResources.0.TopicId 81XXXXe5-e39e-4a1e-b2d4-a778df97d825 \
    --DstResources.0.Alias 别名 \
    --EnableFlag 0 \
    --EtlContent fields_set() \
    --Name 我的数据加工 \
    --TaskId e4fcXXXX-5e8a-4fe0-b52c-76eeca53e9af
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

