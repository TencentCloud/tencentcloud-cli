**Example 1: 查询迁移主题实时数据**



Input: 

```
tccli trocket DescribeMigratingTopicStats --cli-unfold-argument  \
    --TaskId abc \
    --TopicName TopicTest \
    --Namespace 
```

Output: 
```
{
    "Response": {
        "SourceClusterConsumerCount": 0,
        "TargetClusterConsumerCount": 0,
        "RequestId": "abc"
    }
}
```

