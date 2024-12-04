**Example 1: 查询Datahub任务信息**



Input: 

```
tccli ckafka DescribeDatahubTask --cli-unfold-argument  \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "Connections": [],
            "TransformParam": null,
            "SchemaId": "",
            "SchemaName": "",
            "TransformsParam": null,
            "TaskName": "mytask",
            "TaskType": "SOURCE",
            "SourceResource": {
                "Type": "HTTP",
                "KafkaParam": null,
                "EventBusParam": null,
                "MongoDBParam": null,
                "TdwParam": null,
                "EsParam": null,
                "DtsParam": null,
                "ClickHouseParam": null,
                "ClsParam": null,
                "CosParam": null,
                "MySQLParam": null,
                "MqttParam": null,
                "PostgreSQLParam": null,
                "MariaDBParam": null,
                "SQLServerParam": null,
                "CtsdbParam": null,
                "TopicParam": null,
                "ScfParam": null
            },
            "TargetResource": {
                "Type": "KAFKA",
                "KafkaParam": {
                    "Topic": "topic-1",
                    "OffsetType": null,
                    "StartTime": null,
                    "ResourceName": "test-public-network",
                    "ZoneId": 100006,
                    "TopicId": "topic-byp7lpy2",
                    "PartitionNum": 3,
                    "EnableToleration": null,
                    "QpsLimit": 2000,
                    "UseTableMapping": false,
                    "TableMappings": null,
                    "CompressionType": "none",
                    "UseAutoCreateTopic": false,
                    "MsgMultiple": 1,
                    "ConnectorSyncType": "",
                    "KeepPartition": false,
                    "SelfBuilt": false,
                    "Resource": "ckafka-wdvgwwx2"
                },
                "EventBusParam": null,
                "MongoDBParam": null,
                "TdwParam": null,
                "EsParam": null,
                "DtsParam": null,
                "ClickHouseParam": null,
                "ClsParam": null,
                "CosParam": null,
                "MySQLParam": null,
                "MqttParam": null,
                "PostgreSQLParam": null,
                "MariaDBParam": null,
                "SQLServerParam": null,
                "CtsdbParam": null,
                "TopicParam": null,
                "ScfParam": null
            },
            "TaskId": "task-y9799wbn",
            "DatahubId": "datahub-y9799wbn",
            "Status": 1,
            "CreateTime": "2024-12-04 16:22:23",
            "ErrorMessage": "运行中",
            "Tags": []
        },
        "RequestId": "5d584c1c-c41b-4fe1-9d10-b465c586e33e"
    }
}
```

