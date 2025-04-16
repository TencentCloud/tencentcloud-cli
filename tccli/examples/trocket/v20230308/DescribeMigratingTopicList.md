**Example 1: 查询迁移主题列表**



Input: 

```
tccli trocket DescribeMigratingTopicList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "MigrateTopics": [
            {
                "TopicName": "abc",
                "MigrationStatus": "S_RW_D_NA",
                "HealthCheckPassed": true,
                "HealthCheckError": "",
                "Namespace": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

