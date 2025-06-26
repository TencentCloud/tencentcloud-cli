**Example 1: 查询迁移主题列表**



Input: 

```
tccli trocket DescribeMigratingTopicList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "TotalCount": 10,
        "MigrateTopics": [
            {
                "TopicName": "topic-a",
                "MigrationStatus": "S_RW_D_NA",
                "HealthCheckPassed": true,
                "HealthCheckError": "",
                "Namespace": "",
                "FullNamespaceV4": null,
                "NamespaceV4": null,
                "TopicNameV4": null,
                "HealthCheckErrorList": []
            }
        ],
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

