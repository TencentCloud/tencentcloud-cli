**Example 1: 查询Datahub任务列表**



Input: 

```
tccli ckafka DescribeDatahubTasks --cli-unfold-argument  \
    --TaskType SINK \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "TaskList": [
                {
                    "TaskId": "abc",
                    "TaskName": "abc",
                    "TaskType": "abc",
                    "Status": 0,
                    "SourceResource": {
                        "Type": "abc",
                        "KafkaParam": {
                            "SelfBuilt": true,
                            "Resource": "abc",
                            "Topic": "abc",
                            "OffsetType": "abc",
                            "StartTime": 1,
                            "ResourceName": "abc",
                            "ZoneId": 0,
                            "TopicId": "abc",
                            "PartitionNum": 0,
                            "EnableToleration": true,
                            "QpsLimit": 1,
                            "TableMappings": [
                                {
                                    "Database": "abc",
                                    "Table": "abc",
                                    "Topic": "abc",
                                    "TopicId": "abc"
                                }
                            ],
                            "UseTableMapping": true,
                            "UseAutoCreateTopic": true,
                            "CompressionType": "abc",
                            "MsgMultiple": 0,
                            "ConnectorSyncType": "abc",
                            "KeepPartition": true
                        },
                        "EventBusParam": {
                            "Type": "abc",
                            "SelfBuilt": true,
                            "Resource": "abc",
                            "Namespace": "abc",
                            "FunctionName": "abc",
                            "Qualifier": "abc"
                        },
                        "MongoDBParam": {
                            "Database": "abc",
                            "Collection": "abc",
                            "CopyExisting": true,
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "ListeningEvent": "abc",
                            "ReadPreference": "abc",
                            "Pipeline": "abc",
                            "SelfBuilt": true
                        },
                        "EsParam": {
                            "Resource": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "SelfBuilt": true,
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "DropInvalidMessage": true,
                            "Index": "abc",
                            "DateFormat": "abc",
                            "ContentKey": "abc",
                            "DropInvalidJsonMessage": true,
                            "DocumentIdField": "abc",
                            "IndexType": "abc",
                            "DropCls": {
                                "DropInvalidMessageToCls": true,
                                "DropClsRegion": "abc",
                                "DropClsOwneruin": "abc",
                                "DropClsTopicId": "abc",
                                "DropClsLogSet": "abc"
                            },
                            "DatabasePrimaryKey": "abc",
                            "DropDlq": {
                                "Type": "abc",
                                "KafkaParam": {
                                    "SelfBuilt": true,
                                    "Resource": "abc",
                                    "Topic": "abc",
                                    "OffsetType": "abc",
                                    "StartTime": 1,
                                    "ResourceName": "abc",
                                    "ZoneId": 0,
                                    "TopicId": "abc",
                                    "PartitionNum": 0,
                                    "EnableToleration": true,
                                    "QpsLimit": 1,
                                    "TableMappings": [
                                        {
                                            "Database": "abc",
                                            "Table": "abc",
                                            "Topic": "abc",
                                            "TopicId": "abc"
                                        }
                                    ],
                                    "UseTableMapping": true,
                                    "UseAutoCreateTopic": true,
                                    "CompressionType": "abc",
                                    "MsgMultiple": 0,
                                    "ConnectorSyncType": "abc",
                                    "KeepPartition": true
                                },
                                "RetryInterval": 1,
                                "MaxRetryAttempts": 1,
                                "TopicParam": {
                                    "Resource": "abc",
                                    "OffsetType": "abc",
                                    "StartTime": 1,
                                    "TopicId": "abc",
                                    "CompressionType": "abc",
                                    "UseAutoCreateTopic": true,
                                    "MsgMultiple": 0
                                },
                                "DlqType": "abc"
                            },
                            "RecordMappingList": [
                                {
                                    "ColumnName": "abc",
                                    "JsonKey": "abc"
                                }
                            ],
                            "DateField": "abc",
                            "RecordMappingMode": "abc"
                        },
                        "TdwParam": {
                            "Bid": "abc",
                            "Tid": "abc",
                            "IsDomestic": true,
                            "TdwHost": "abc",
                            "TdwPort": 0
                        },
                        "DtsParam": {
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "Topic": "abc",
                            "GroupId": "abc",
                            "GroupUser": "abc",
                            "GroupPassword": "abc",
                            "TranSql": true
                        },
                        "ClickHouseParam": {
                            "Cluster": "abc",
                            "Database": "abc",
                            "Table": "abc",
                            "Schema": [
                                {
                                    "ColumnName": "abc",
                                    "JsonKey": "abc",
                                    "Type": "abc",
                                    "AllowNull": true
                                }
                            ],
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "SelfBuilt": true,
                            "DropInvalidMessage": true,
                            "Type": "abc",
                            "DropCls": {
                                "DropInvalidMessageToCls": true,
                                "DropClsRegion": "abc",
                                "DropClsOwneruin": "abc",
                                "DropClsTopicId": "abc",
                                "DropClsLogSet": "abc"
                            },
                            "BatchSize": 0,
                            "ConsumerFetchMinBytes": 0,
                            "ConsumerFetchMaxWaitMs": 0
                        },
                        "ClsParam": {
                            "DecodeJson": true,
                            "Resource": "abc",
                            "LogSet": "abc",
                            "ContentKey": "abc",
                            "TimeField": "abc"
                        },
                        "CosParam": {
                            "BucketName": "abc",
                            "Region": "abc",
                            "ObjectKey": "abc",
                            "AggregateBatchSize": 1,
                            "AggregateInterval": 1,
                            "FormatOutputType": "abc",
                            "ObjectKeyPrefix": "abc",
                            "DirectoryTimeFormat": "abc"
                        },
                        "MySQLParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc",
                            "DdlTopic": "abc",
                            "DataSourceMonitorMode": "abc",
                            "DataSourceMonitorResource": "abc",
                            "DataSourceIncrementMode": "abc",
                            "DataSourceIncrementColumn": "abc",
                            "DataSourceStartFrom": "abc",
                            "DataTargetInsertMode": "abc",
                            "DataTargetPrimaryKeyField": "abc",
                            "DataTargetRecordMapping": [
                                {
                                    "JsonKey": "abc",
                                    "Type": "abc",
                                    "AllowNull": true,
                                    "ColumnName": "abc",
                                    "ExtraInfo": "abc",
                                    "ColumnSize": "abc",
                                    "DecimalDigits": "abc",
                                    "AutoIncrement": true,
                                    "DefaultValue": "abc"
                                }
                            ],
                            "TopicRegex": "abc",
                            "TopicReplacement": "abc",
                            "KeyColumns": "abc",
                            "DropInvalidMessage": true,
                            "DropCls": {
                                "DropInvalidMessageToCls": true,
                                "DropClsRegion": "abc",
                                "DropClsOwneruin": "abc",
                                "DropClsTopicId": "abc",
                                "DropClsLogSet": "abc"
                            },
                            "OutputFormat": "abc",
                            "IsTablePrefix": true,
                            "IncludeContentChanges": "abc",
                            "IncludeQuery": true,
                            "RecordWithSchema": true,
                            "SignalDatabase": "abc",
                            "IsTableRegular": true,
                            "SignalTable": "abc",
                            "DateTimeZone": "abc",
                            "SelfBuilt": true
                        },
                        "PostgreSQLParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "PluginName": "abc",
                            "SnapshotMode": "abc",
                            "DataFormat": "abc",
                            "DataTargetInsertMode": "abc",
                            "DataTargetPrimaryKeyField": "abc",
                            "DataTargetRecordMapping": [
                                {
                                    "JsonKey": "abc",
                                    "Type": "abc",
                                    "AllowNull": true,
                                    "ColumnName": "abc",
                                    "ExtraInfo": "abc",
                                    "ColumnSize": "abc",
                                    "DecimalDigits": "abc",
                                    "AutoIncrement": true,
                                    "DefaultValue": "abc"
                                }
                            ],
                            "DropInvalidMessage": true,
                            "IsTableRegular": true,
                            "KeyColumns": "abc",
                            "RecordWithSchema": true
                        },
                        "TopicParam": {
                            "Resource": "abc",
                            "OffsetType": "abc",
                            "StartTime": 1,
                            "TopicId": "abc",
                            "CompressionType": "abc",
                            "UseAutoCreateTopic": true,
                            "MsgMultiple": 0
                        },
                        "MariaDBParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc",
                            "KeyColumns": "abc",
                            "IsTablePrefix": true,
                            "OutputFormat": "abc",
                            "IncludeContentChanges": "abc",
                            "IncludeQuery": true,
                            "RecordWithSchema": true
                        },
                        "SQLServerParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc"
                        },
                        "CtsdbParam": {
                            "Resource": "abc",
                            "CtsdbMetric": "abc"
                        },
                        "ScfParam": {
                            "FunctionName": "abc",
                            "Namespace": "abc",
                            "Qualifier": "abc",
                            "BatchSize": 0,
                            "MaxRetries": 0
                        },
                        "MqttParam": {
                            "Topics": "abc",
                            "CleanSession": true,
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "Qos": 0,
                            "MaxTasks": 0,
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "SelfBuilt": true
                        }
                    },
                    "TargetResource": {
                        "Type": "abc",
                        "KafkaParam": {
                            "SelfBuilt": true,
                            "Resource": "abc",
                            "Topic": "abc",
                            "OffsetType": "abc",
                            "StartTime": 1,
                            "ResourceName": "abc",
                            "ZoneId": 0,
                            "TopicId": "abc",
                            "PartitionNum": 0,
                            "EnableToleration": true,
                            "QpsLimit": 1,
                            "TableMappings": [
                                {
                                    "Database": "abc",
                                    "Table": "abc",
                                    "Topic": "abc",
                                    "TopicId": "abc"
                                }
                            ],
                            "UseTableMapping": true,
                            "UseAutoCreateTopic": true,
                            "CompressionType": "abc",
                            "MsgMultiple": 0,
                            "ConnectorSyncType": "abc",
                            "KeepPartition": true
                        },
                        "EventBusParam": {
                            "Type": "abc",
                            "SelfBuilt": true,
                            "Resource": "abc",
                            "Namespace": "abc",
                            "FunctionName": "abc",
                            "Qualifier": "abc"
                        },
                        "MongoDBParam": {
                            "Database": "abc",
                            "Collection": "abc",
                            "CopyExisting": true,
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "ListeningEvent": "abc",
                            "ReadPreference": "abc",
                            "Pipeline": "abc",
                            "SelfBuilt": true
                        },
                        "EsParam": {
                            "Resource": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "SelfBuilt": true,
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "DropInvalidMessage": true,
                            "Index": "abc",
                            "DateFormat": "abc",
                            "ContentKey": "abc",
                            "DropInvalidJsonMessage": true,
                            "DocumentIdField": "abc",
                            "IndexType": "abc",
                            "DatabasePrimaryKey": "abc",
                            "DropDlq": {
                                "Type": "abc",
                                "RetryInterval": 1,
                                "MaxRetryAttempts": 1,
                                "TopicParam": {
                                    "Resource": "abc",
                                    "OffsetType": "abc",
                                    "StartTime": 1,
                                    "TopicId": "abc",
                                    "CompressionType": "abc",
                                    "UseAutoCreateTopic": true,
                                    "MsgMultiple": 0
                                },
                                "DlqType": "abc"
                            },
                            "RecordMappingList": [
                                {
                                    "ColumnName": "abc",
                                    "JsonKey": "abc"
                                }
                            ],
                            "DateField": "abc",
                            "RecordMappingMode": "abc"
                        },
                        "TdwParam": {
                            "Bid": "abc",
                            "Tid": "abc",
                            "IsDomestic": true,
                            "TdwHost": "abc",
                            "TdwPort": 0
                        },
                        "DtsParam": {
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "Topic": "abc",
                            "GroupId": "abc",
                            "GroupUser": "abc",
                            "GroupPassword": "abc",
                            "TranSql": true
                        },
                        "ClickHouseParam": {
                            "Cluster": "abc",
                            "Database": "abc",
                            "Table": "abc",
                            "Schema": [
                                {
                                    "ColumnName": "abc",
                                    "JsonKey": "abc",
                                    "Type": "abc",
                                    "AllowNull": true
                                }
                            ],
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "SelfBuilt": true,
                            "DropInvalidMessage": true,
                            "Type": "abc",
                            "BatchSize": 0,
                            "ConsumerFetchMinBytes": 0,
                            "ConsumerFetchMaxWaitMs": 0
                        },
                        "ClsParam": {
                            "DecodeJson": true,
                            "Resource": "abc",
                            "LogSet": "abc",
                            "ContentKey": "abc",
                            "TimeField": "abc"
                        },
                        "CosParam": {
                            "BucketName": "abc",
                            "Region": "abc",
                            "ObjectKey": "abc",
                            "AggregateBatchSize": 1,
                            "AggregateInterval": 1,
                            "FormatOutputType": "abc",
                            "ObjectKeyPrefix": "abc",
                            "DirectoryTimeFormat": "abc"
                        },
                        "MySQLParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc",
                            "DdlTopic": "abc",
                            "DataSourceMonitorMode": "abc",
                            "DataSourceMonitorResource": "abc",
                            "DataSourceIncrementMode": "abc",
                            "DataSourceIncrementColumn": "abc",
                            "DataSourceStartFrom": "abc",
                            "DataTargetInsertMode": "abc",
                            "DataTargetPrimaryKeyField": "abc",
                            "DataTargetRecordMapping": [
                                {
                                    "JsonKey": "abc",
                                    "Type": "abc",
                                    "AllowNull": true,
                                    "ColumnName": "abc",
                                    "ExtraInfo": "abc",
                                    "ColumnSize": "abc",
                                    "DecimalDigits": "abc",
                                    "AutoIncrement": true,
                                    "DefaultValue": "abc"
                                }
                            ],
                            "TopicRegex": "abc",
                            "TopicReplacement": "abc",
                            "KeyColumns": "abc",
                            "DropInvalidMessage": true,
                            "OutputFormat": "abc",
                            "IsTablePrefix": true,
                            "IncludeContentChanges": "abc",
                            "IncludeQuery": true,
                            "RecordWithSchema": true,
                            "SignalDatabase": "abc",
                            "IsTableRegular": true,
                            "SignalTable": "abc",
                            "DateTimeZone": "abc",
                            "SelfBuilt": true
                        },
                        "PostgreSQLParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "PluginName": "abc",
                            "SnapshotMode": "abc",
                            "DataFormat": "abc",
                            "DataTargetInsertMode": "abc",
                            "DataTargetPrimaryKeyField": "abc",
                            "DropInvalidMessage": true,
                            "IsTableRegular": true,
                            "KeyColumns": "abc",
                            "RecordWithSchema": true
                        },
                        "MariaDBParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc",
                            "KeyColumns": "abc",
                            "IsTablePrefix": true,
                            "OutputFormat": "abc",
                            "IncludeContentChanges": "abc",
                            "IncludeQuery": true,
                            "RecordWithSchema": true
                        },
                        "SQLServerParam": {
                            "Database": "abc",
                            "Table": "abc",
                            "Resource": "abc",
                            "SnapshotMode": "abc"
                        },
                        "CtsdbParam": {
                            "Resource": "abc",
                            "CtsdbMetric": "abc"
                        },
                        "ScfParam": {
                            "FunctionName": "abc",
                            "Namespace": "abc",
                            "Qualifier": "abc",
                            "BatchSize": 0,
                            "MaxRetries": 0
                        },
                        "MqttParam": {
                            "Topics": "abc",
                            "CleanSession": true,
                            "Resource": "abc",
                            "Ip": "abc",
                            "Port": 0,
                            "UserName": "abc",
                            "Password": "abc",
                            "Qos": 0,
                            "MaxTasks": 0,
                            "ServiceVip": "abc",
                            "UniqVpcId": "abc",
                            "SelfBuilt": true
                        }
                    },
                    "CreateTime": "abc",
                    "ErrorMessage": "abc",
                    "TaskProgress": 0,
                    "TaskCurrentStep": "abc",
                    "DatahubId": "abc",
                    "StepList": [
                        "abc"
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

