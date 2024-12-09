**Example 1: 查询Datahub任务列表**



Input: 

```
tccli ckafka DescribeDatahubTasks --cli-unfold-argument  \
    --TaskType SOURCE \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "TaskList": [
                {
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
                            "TopicId": null,
                            "PartitionNum": null,
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
                    "TaskProgress": 36,
                    "TaskCurrentStep": "FINISH",
                    "StepList": []
                }
            ]
        },
        "RequestId": "08e8fe64-062f-4e15-88fd-aecdf848bf3e"
    }
}
```

