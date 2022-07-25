**Example 1: 查询Datahub任务信息**



Input: 

```
tccli ckafka DescribeDatahubTask --cli-unfold-argument  \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "Status": 0,
            "TransformsParam": {
                "OutputFormat": "xx",
                "SourceType": "xx",
                "FilterParam": [
                    {
                        "MatchMode": "xx",
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "FailureParam": {
                    "RetryInterval": 1,
                    "Type": "xx",
                    "MaxRetryAttempts": 1,
                    "KafkaParam": {
                        "TopicId": "xx",
                        "Resource": "xx",
                        "PartitionNum": 0,
                        "QpsLimit": 1,
                        "EnableToleration": true,
                        "SelfBuilt": true,
                        "Topic": "xx",
                        "OffsetType": "xx",
                        "StartTime": 1,
                        "ResourceName": "xx",
                        "ZoneId": 0
                    }
                },
                "Content": "xx",
                "Result": "xx",
                "FieldChain": [
                    {
                        "AnalyseJsonResult": "xx",
                        "SecondaryAnalyseJsonResult": "xx",
                        "Analyse": {
                            "Regex": "xx",
                            "InputValueType": "xx",
                            "InputValue": "xx",
                            "Format": "xx"
                        },
                        "SMT": [
                            {
                                "ValueOperates": [
                                    {
                                        "Date": {
                                            "TargetType": "xx",
                                            "TimeZone": "xx",
                                            "Format": "xx"
                                        },
                                        "Substr": {
                                            "Start": 0,
                                            "End": 0
                                        },
                                        "Type": "xx",
                                        "Replace": {
                                            "NewValue": "xx",
                                            "OldValue": "xx"
                                        }
                                    }
                                ],
                                "Value": "xx",
                                "SchemeType": "xx",
                                "OriginalValue": "xx",
                                "Key": "xx",
                                "Operate": "xx",
                                "ValueOperate": {
                                    "Date": {
                                        "TargetType": "xx",
                                        "TimeZone": "xx",
                                        "Format": "xx"
                                    },
                                    "Substr": {
                                        "Start": 0,
                                        "End": 0
                                    },
                                    "Type": "xx",
                                    "Replace": {
                                        "NewValue": "xx",
                                        "OldValue": "xx"
                                    }
                                }
                            }
                        ],
                        "SecondaryAnalyseResult": [
                            {
                                "ValueOperates": [
                                    {
                                        "Date": {
                                            "TargetType": "xx",
                                            "TimeZone": "xx",
                                            "Format": "xx"
                                        },
                                        "Substr": {
                                            "Start": 0,
                                            "End": 0
                                        },
                                        "Type": "xx",
                                        "Replace": {
                                            "NewValue": "xx",
                                            "OldValue": "xx"
                                        }
                                    }
                                ],
                                "Value": "xx",
                                "SchemeType": "xx",
                                "OriginalValue": "xx",
                                "Key": "xx",
                                "Operate": "xx"
                            }
                        ],
                        "SecondaryAnalyse": {
                            "Regex": "xx"
                        },
                        "Result": "xx",
                        "AnalyseResult": [
                            {
                                "OriginalValue": "xx",
                                "Operate": "xx",
                                "Value": "xx",
                                "Key": "xx",
                                "SchemeType": "xx"
                            }
                        ]
                    }
                ]
            },
            "SchemaId": "xx",
            "DatahubId": "xx",
            "TargetResource": {
                "EventBusParam": {
                    "Resource": "xx",
                    "FunctionName": "xx",
                    "Namespace": "xx",
                    "SelfBuilt": true,
                    "Type": "xx",
                    "Qualifier": "xx"
                },
                "ClickHouseParam": {
                    "UserName": "xx",
                    "Resource": "xx",
                    "UniqVpcId": "xx",
                    "Database": "xx",
                    "Ip": "xx",
                    "DropInvalidMessage": true,
                    "SelfBuilt": true,
                    "Cluster": "xx",
                    "ServiceVip": "xx",
                    "Table": "xx",
                    "Password": "xx",
                    "Type": "xx",
                    "Port": 0,
                    "Schema": [
                        {
                            "ColumnName": "xx",
                            "Type": "xx",
                            "JsonKey": "xx",
                            "AllowNull": true
                        }
                    ]
                },
                "TdwParam": {
                    "Tid": "xx",
                    "Bid": "xx"
                },
                "MySQLParam": {
                    "DdlTopic": "xx",
                    "Database": "xx",
                    "Resource": "xx",
                    "Table": "xx",
                    "SnapshotMode": "xx"
                },
                "CosParam": {
                    "FormatOutputType": "xx",
                    "ObjectKey": "xx",
                    "BucketName": "xx",
                    "AggregateBatchSize": 1,
                    "Region": "xx",
                    "AggregateInterval": 1
                },
                "TopicParam": {
                    "OffsetType": "xx",
                    "Resource": "xx",
                    "StartTime": 1
                },
                "KafkaParam": {
                    "TopicId": "xx",
                    "Resource": "xx",
                    "PartitionNum": 0,
                    "QpsLimit": 1,
                    "EnableToleration": true,
                    "SelfBuilt": true,
                    "Topic": "xx",
                    "OffsetType": "xx",
                    "StartTime": 1,
                    "ResourceName": "xx",
                    "ZoneId": 0
                },
                "EsParam": {
                    "UserName": "xx",
                    "Index": "xx",
                    "Resource": "xx",
                    "UniqVpcId": "xx",
                    "DropInvalidMessage": true,
                    "DateFormat": "xx",
                    "SelfBuilt": true,
                    "ServiceVip": "xx",
                    "Password": "xx",
                    "DropInvalidJsonMessage": true,
                    "Port": 0,
                    "ContentKey": "xx",
                    "DocumentIdField": "xx"
                },
                "DtsParam": {
                    "Resource": "xx",
                    "Ip": "xx",
                    "GroupId": "xx",
                    "Topic": "xx",
                    "GroupUser": "xx",
                    "GroupPassword": "xx",
                    "Port": 0
                },
                "MongoDBParam": {
                    "UserName": "xx",
                    "CopyExisting": true,
                    "Pipeline": "xx",
                    "ListeningEvent": "xx",
                    "Resource": "xx",
                    "ReadPreference": "xx",
                    "Database": "xx",
                    "Ip": "xx",
                    "Collection": "xx",
                    "SelfBuilt": true,
                    "Password": "xx",
                    "Port": 0
                },
                "PostgreSQLParam": {
                    "Table": "xx",
                    "PluginName": "xx",
                    "Resource": "xx",
                    "SnapshotMode": "xx",
                    "Database": "xx"
                },
                "Type": "xx",
                "ClsParam": {
                    "LogSet": "xx",
                    "Resource": "xx",
                    "ContentKey": "xx",
                    "DecodeJson": true
                }
            },
            "Connections": [
                {
                    "TopicId": "xx",
                    "TopicName": "xx",
                    "GroupId": "xx"
                }
            ],
            "TransformParam": {
                "Regex": "xx",
                "OutputFormat": "xx",
                "SourceType": "xx",
                "FilterParam": [
                    {
                        "MatchMode": "xx",
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "UseEventBus": true,
                "FailureParam": {
                    "RetryInterval": 1,
                    "Type": "xx",
                    "MaxRetryAttempts": 1,
                    "KafkaParam": {
                        "TopicId": "xx",
                        "Resource": "xx",
                        "PartitionNum": 0,
                        "QpsLimit": 1,
                        "EnableToleration": true,
                        "SelfBuilt": true,
                        "Topic": "xx",
                        "OffsetType": "xx",
                        "StartTime": 1,
                        "ResourceName": "xx",
                        "ZoneId": 0
                    }
                },
                "Content": "xx",
                "AnalysisFormat": "xx",
                "MapParam": [
                    {
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "AnalyseResult": [
                    {
                        "Type": "xx",
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "Result": "xx"
            },
            "TaskId": "xx",
            "TaskType": "xx",
            "SourceResource": {
                "EventBusParam": {
                    "Resource": "xx",
                    "FunctionName": "xx",
                    "Namespace": "xx",
                    "SelfBuilt": true,
                    "Type": "xx",
                    "Qualifier": "xx"
                },
                "ClickHouseParam": {
                    "UserName": "xx",
                    "Resource": "xx",
                    "UniqVpcId": "xx",
                    "Database": "xx",
                    "Ip": "xx",
                    "DropInvalidMessage": true,
                    "SelfBuilt": true,
                    "Cluster": "xx",
                    "ServiceVip": "xx",
                    "Table": "xx",
                    "Password": "xx",
                    "Type": "xx",
                    "Port": 0,
                    "Schema": [
                        {
                            "ColumnName": "xx",
                            "Type": "xx",
                            "JsonKey": "xx",
                            "AllowNull": true
                        }
                    ]
                },
                "TdwParam": {
                    "Tid": "xx",
                    "Bid": "xx"
                },
                "MySQLParam": {
                    "DdlTopic": "xx",
                    "Database": "xx",
                    "Resource": "xx",
                    "Table": "xx",
                    "SnapshotMode": "xx"
                },
                "CosParam": {
                    "FormatOutputType": "xx",
                    "ObjectKey": "xx",
                    "BucketName": "xx",
                    "AggregateBatchSize": 1,
                    "Region": "xx",
                    "AggregateInterval": 1
                },
                "TopicParam": {
                    "OffsetType": "xx",
                    "Resource": "xx",
                    "StartTime": 1
                },
                "EsParam": {
                    "UserName": "xx",
                    "Index": "xx",
                    "Resource": "xx",
                    "UniqVpcId": "xx",
                    "DropInvalidMessage": true,
                    "DateFormat": "xx",
                    "SelfBuilt": true,
                    "ServiceVip": "xx",
                    "Password": "xx",
                    "DropInvalidJsonMessage": true,
                    "Port": 0,
                    "ContentKey": "xx",
                    "DocumentIdField": "xx"
                },
                "DtsParam": {
                    "Resource": "xx",
                    "Ip": "xx",
                    "GroupId": "xx",
                    "Topic": "xx",
                    "GroupUser": "xx",
                    "GroupPassword": "xx",
                    "Port": 0
                },
                "MongoDBParam": {
                    "UserName": "xx",
                    "CopyExisting": true,
                    "Pipeline": "xx",
                    "ListeningEvent": "xx",
                    "Resource": "xx",
                    "ReadPreference": "xx",
                    "Database": "xx",
                    "Ip": "xx",
                    "Collection": "xx",
                    "SelfBuilt": true,
                    "Password": "xx",
                    "Port": 0
                },
                "PostgreSQLParam": {
                    "Table": "xx",
                    "PluginName": "xx",
                    "Resource": "xx",
                    "SnapshotMode": "xx",
                    "Database": "xx"
                },
                "Type": "xx",
                "ClsParam": {
                    "LogSet": "xx",
                    "Resource": "xx",
                    "ContentKey": "xx",
                    "DecodeJson": true
                }
            },
            "SchemaName": "xx",
            "TaskName": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

