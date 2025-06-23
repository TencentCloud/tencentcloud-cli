**Example 1: 查询迁移主题实时数据**



Input: 

```
tccli trocket DescribeMigratingTopicStats --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --TopicName TopicTest \
    --Namespace 
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "SourceClusterConsumerCount": 0,
        "TargetClusterConsumerCount": 0,
        "SourceClusterConsumerGroups": [],
        "TargetClusterConsumerGroups": [],
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

