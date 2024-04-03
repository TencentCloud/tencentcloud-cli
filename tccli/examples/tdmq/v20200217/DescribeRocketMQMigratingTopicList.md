**Example 1: 标准请求**

标准请求

Input: 

```
tccli tdmq DescribeRocketMQMigratingTopicList --cli-unfold-argument  \
    --TaskId 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "MigrateTopics": [
            {
                "HealthCheckPassed": false,
                "MigrationStatus": "S_RW_D_NA",
                "TopicName": "six"
            }
        ],
        "RequestId": "f92642b4-e1bc-451f-ac4f-c639af4f6355",
        "TotalCount": 1
    }
}
```

**Example 2: 查询迁移中的主题列表**

查询迁移中的主题列表

Input: 

```
tccli tdmq DescribeRocketMQMigratingTopicList --cli-unfold-argument  \
    --TaskId 700000780519-o4n3m5g97wgr-3391d15d \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "MigrateTopics": [
            {
                "HealthCheckError": null,
                "HealthCheckPassed": false,
                "MigrationStatus": "S_RW_D_NA",
                "Namespace": "tdmq_default",
                "TopicName": "Topic_11334"
            },
            {
                "HealthCheckError": "TargetTopicHasNoMessagesIn5Minutes",
                "HealthCheckPassed": false,
                "MigrationStatus": "S_R_D_RW",
                "Namespace": "tdmq_default",
                "TopicName": "Topic_12371"
            },
            {
                "HealthCheckError": "TargetTopicHasNewMessagesIn5Minutes",
                "HealthCheckPassed": true,
                "MigrationStatus": "S_RW_D_R",
                "Namespace": "tdmq_default",
                "TopicName": "Topic_18637"
            },
            {
                "HealthCheckError": "TargetTopicHasNewMessagesIn5Minutes",
                "HealthCheckPassed": true,
                "MigrationStatus": "S_RW_D_NA",
                "Namespace": "tdmq_default",
                "TopicName": "Topic_18786"
            }
        ],
        "RequestId": "6191def5-5812-4339-b834-b2426e3a02b0",
        "TotalCount": 4
    }
}
```

