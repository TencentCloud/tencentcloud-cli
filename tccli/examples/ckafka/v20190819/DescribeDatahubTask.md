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
                "KeepMetadata": true,
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
                    "TopicParam": {
                        "TopicId": "xx",
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
                        "UseTableMapping": true,
                        "ResourceName": "xx",
                        "ZoneId": 0,
                        "TableMappings": [
                            {
                                "Topic": "xx",
                                "Table": "xx",
                                "TopicId": "xx",
                                "Database": "xx"
                            }
                        ]
                    },
                    "MaxRetryAttempts": 1,
                    "Type": "xx",
                    "DlqType": "xx"
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
                                        "Result": "xx",
                                        "Replace": {
                                            "NewValue": "xx",
                                            "OldValue": "xx"
                                        },
                                        "Substr": {
                                            "Start": 0,
                                            "End": 0
                                        },
                                        "Split": {
                                            "Regex": "xx"
                                        },
                                        "KV": {
                                            "Regex": "xx",
                                            "KeepOriginalKey": "xx",
                                            "Delimiter": "xx"
                                        },
                                        "Date": {
                                            "TargetType": "xx",
                                            "TimeZone": "xx",
                                            "Format": "xx"
                                        },
                                        "Type": "xx",
                                        "RegexReplace": {
                                            "Regex": "xx",
                                            "NewValue": "xx"
                                        }
                                    }
                                ],
                                "Value": "xx",
                                "SchemeType": "xx",
                                "OriginalValue": "xx",
                                "Key": "xx",
                                "Operate": "xx",
                                "ValueOperate": {
                                    "Result": "xx",
                                    "Replace": {
                                        "NewValue": "xx",
                                        "OldValue": "xx"
                                    },
                                    "Substr": {
                                        "Start": 0,
                                        "End": 0
                                    },
                                    "Split": {
                                        "Regex": "xx"
                                    },
                                    "KV": {
                                        "Regex": "xx",
                                        "KeepOriginalKey": "xx",
                                        "Delimiter": "xx"
                                    },
                                    "Date": {
                                        "TargetType": "xx",
                                        "TimeZone": "xx",
                                        "Format": "xx"
                                    },
                                    "Type": "xx",
                                    "RegexReplace": {
                                        "Regex": "xx",
                                        "NewValue": "xx"
                                    }
                                }
                            }
                        ],
                        "SecondaryAnalyseResult": [
                            {
                                "ValueOperates": [
                                    {
                                        "Result": "xx",
                                        "Replace": {
                                            "NewValue": "xx",
                                            "OldValue": "xx"
                                        },
                                        "Substr": {
                                            "Start": 0,
                                            "End": 0
                                        },
                                        "Split": {
                                            "Regex": "xx"
                                        },
                                        "KV": {
                                            "Regex": "xx",
                                            "KeepOriginalKey": "xx",
                                            "Delimiter": "xx"
                                        },
                                        "Date": {
                                            "TargetType": "xx",
                                            "TimeZone": "xx",
                                            "Format": "xx"
                                        },
                                        "Type": "xx",
                                        "RegexReplace": {
                                            "Regex": "xx",
                                            "NewValue": "xx"
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
                ],
                "RowParam": {
                    "RowContent": "xx",
                    "KeyValueDelimiter": "xx",
                    "EntryDelimiter": "xx"
                }
            },
            "Tags": [
                {
                    "TagKey": "xx",
                    "TagValue": "xx"
                }
            ],
            "SchemaId": "xx",
            "ErrorMessage": "xx",
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
                    "DropCls": {
                        "DropInvalidMessageToCls": true,
                        "DropClsTopicId": "xx",
                        "DropClsRegion": "xx",
                        "DropClsLogSet": "xx",
                        "DropClsOwneruin": "xx"
                    },
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
                "CtsdbParam": {
                    "Resource": "xx",
                    "CtsdbMetric": "xx"
                },
                "TdwParam": {
                    "Tid": "xx",
                    "Bid": "xx",
                    "TdwHost": "xx",
                    "IsDomestic": true,
                    "TdwPort": 0
                },
                "MySQLParam": {
                    "OutputFormat": "xx",
                    "DropCls": {
                        "DropInvalidMessageToCls": true,
                        "DropClsTopicId": "xx",
                        "DropClsRegion": "xx",
                        "DropClsLogSet": "xx",
                        "DropClsOwneruin": "xx"
                    },
                    "DataSourceIncrementMode": "xx",
                    "DataSourceMonitorMode": "xx",
                    "IncludeContentChanges": "xx",
                    "DataTargetPrimaryKeyField": "xx",
                    "TopicReplacement": "xx",
                    "TopicRegex": "xx",
                    "DataTargetInsertMode": "xx",
                    "DataSourceIncrementColumn": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "DdlTopic": "xx",
                    "IncludeQuery": true,
                    "DataTargetRecordMapping": [
                        {
                            "JsonKey": "xx",
                            "ColumnName": "xx",
                            "AutoIncrement": true,
                            "DefaultValue": "xx",
                            "ExtraInfo": "xx",
                            "AllowNull": true,
                            "ColumnSize": "xx",
                            "Type": "xx",
                            "DecimalDigits": "xx"
                        }
                    ],
                    "DataSourceMonitorResource": "xx",
                    "KeyColumns": "xx",
                    "RecordWithSchema": true,
                    "DropInvalidMessage": true,
                    "SnapshotMode": "xx",
                    "IsTablePrefix": true,
                    "Table": "xx",
                    "DataSourceStartFrom": "xx"
                },
                "CosParam": {
                    "FormatOutputType": "xx",
                    "DirectoryTimeFormat": "xx",
                    "ObjectKey": "xx",
                    "BucketName": "xx",
                    "AggregateBatchSize": 1,
                    "ObjectKeyPrefix": "xx",
                    "Region": "xx",
                    "AggregateInterval": 1
                },
                "TopicParam": {
                    "TopicId": "xx",
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
                    "UseTableMapping": true,
                    "ResourceName": "xx",
                    "ZoneId": 0,
                    "TableMappings": [
                        {
                            "Topic": "xx",
                            "Table": "xx",
                            "TopicId": "xx",
                            "Database": "xx"
                        }
                    ]
                },
                "EsParam": {
                    "UserName": "xx",
                    "Index": "xx",
                    "Resource": "xx",
                    "IndexType": "xx",
                    "UniqVpcId": "xx",
                    "DropInvalidMessage": true,
                    "DateFormat": "xx",
                    "SelfBuilt": true,
                    "DropInvalidJsonMessage": true,
                    "ServiceVip": "xx",
                    "DropCls": {
                        "DropInvalidMessageToCls": true,
                        "DropClsTopicId": "xx",
                        "DropClsRegion": "xx",
                        "DropClsLogSet": "xx",
                        "DropClsOwneruin": "xx"
                    },
                    "Password": "xx",
                    "Port": 0,
                    "DatabasePrimaryKey": "xx",
                    "ContentKey": "xx",
                    "DocumentIdField": "xx"
                },
                "DtsParam": {
                    "Resource": "xx",
                    "Ip": "xx",
                    "TranSql": true,
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
                    "DataTargetInsertMode": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "DropInvalidMessage": true,
                    "DataTargetRecordMapping": [
                        {
                            "JsonKey": "xx",
                            "ColumnName": "xx",
                            "AutoIncrement": true,
                            "DefaultValue": "xx",
                            "ExtraInfo": "xx",
                            "AllowNull": true,
                            "ColumnSize": "xx",
                            "Type": "xx",
                            "DecimalDigits": "xx"
                        }
                    ],
                    "SnapshotMode": "xx",
                    "PluginName": "xx",
                    "DataFormat": "xx",
                    "KeyColumns": "xx",
                    "RecordWithSchema": true,
                    "DataTargetPrimaryKeyField": "xx",
                    "Table": "xx",
                    "IsTableRegular": true
                },
                "SQLServerParam": {
                    "Table": "xx",
                    "SnapshotMode": "xx",
                    "Resource": "xx",
                    "Database": "xx"
                },
                "MariaDBParam": {
                    "OutputFormat": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "IncludeQuery": true,
                    "SnapshotMode": "xx",
                    "KeyColumns": "xx",
                    "IsTablePrefix": true,
                    "IncludeContentChanges": "xx",
                    "Table": "xx",
                    "RecordWithSchema": true
                },
                "Type": "xx",
                "ClsParam": {
                    "LogSet": "xx",
                    "TimeField": "xx",
                    "Resource": "xx",
                    "ContentKey": "xx",
                    "DecodeJson": true
                }
            },
            "TaskType": "xx",
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
                    "TopicParam": {
                        "TopicId": "xx",
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
                        "UseTableMapping": true,
                        "ResourceName": "xx",
                        "ZoneId": 0,
                        "TableMappings": [
                            {
                                "Topic": "xx",
                                "Table": "xx",
                                "TopicId": "xx",
                                "Database": "xx"
                            }
                        ]
                    },
                    "MaxRetryAttempts": 1,
                    "Type": "xx",
                    "DlqType": "xx"
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
            "DatahubId": "xx",
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
                "CtsdbParam": {
                    "Resource": "xx",
                    "CtsdbMetric": "xx"
                },
                "TdwParam": {
                    "Tid": "xx",
                    "Bid": "xx",
                    "TdwHost": "xx",
                    "IsDomestic": true,
                    "TdwPort": 0
                },
                "MySQLParam": {
                    "OutputFormat": "xx",
                    "DataSourceIncrementMode": "xx",
                    "DataSourceMonitorMode": "xx",
                    "IncludeContentChanges": "xx",
                    "DataTargetPrimaryKeyField": "xx",
                    "TopicReplacement": "xx",
                    "TopicRegex": "xx",
                    "DataTargetInsertMode": "xx",
                    "DataSourceIncrementColumn": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "DdlTopic": "xx",
                    "IncludeQuery": true,
                    "DataTargetRecordMapping": [
                        {
                            "JsonKey": "xx",
                            "ColumnName": "xx",
                            "AutoIncrement": true,
                            "DefaultValue": "xx",
                            "ExtraInfo": "xx",
                            "AllowNull": true,
                            "ColumnSize": "xx",
                            "Type": "xx",
                            "DecimalDigits": "xx"
                        }
                    ],
                    "DataSourceMonitorResource": "xx",
                    "KeyColumns": "xx",
                    "RecordWithSchema": true,
                    "DropInvalidMessage": true,
                    "SnapshotMode": "xx",
                    "IsTablePrefix": true,
                    "Table": "xx",
                    "DataSourceStartFrom": "xx"
                },
                "CosParam": {
                    "FormatOutputType": "xx",
                    "DirectoryTimeFormat": "xx",
                    "ObjectKey": "xx",
                    "BucketName": "xx",
                    "AggregateBatchSize": 1,
                    "ObjectKeyPrefix": "xx",
                    "Region": "xx",
                    "AggregateInterval": 1
                },
                "EsParam": {
                    "UserName": "xx",
                    "Index": "xx",
                    "Resource": "xx",
                    "IndexType": "xx",
                    "UniqVpcId": "xx",
                    "DropInvalidMessage": true,
                    "DateFormat": "xx",
                    "SelfBuilt": true,
                    "ServiceVip": "xx",
                    "DatabasePrimaryKey": "xx",
                    "Password": "xx",
                    "DropInvalidJsonMessage": true,
                    "Port": 0,
                    "ContentKey": "xx",
                    "DocumentIdField": "xx"
                },
                "DtsParam": {
                    "Resource": "xx",
                    "Ip": "xx",
                    "TranSql": true,
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
                    "DataTargetInsertMode": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "DropInvalidMessage": true,
                    "SnapshotMode": "xx",
                    "PluginName": "xx",
                    "DataFormat": "xx",
                    "KeyColumns": "xx",
                    "RecordWithSchema": true,
                    "DataTargetPrimaryKeyField": "xx",
                    "Table": "xx",
                    "IsTableRegular": true
                },
                "SQLServerParam": {
                    "Table": "xx",
                    "SnapshotMode": "xx",
                    "Resource": "xx",
                    "Database": "xx"
                },
                "MariaDBParam": {
                    "OutputFormat": "xx",
                    "Resource": "xx",
                    "Database": "xx",
                    "IncludeQuery": true,
                    "SnapshotMode": "xx",
                    "KeyColumns": "xx",
                    "IsTablePrefix": true,
                    "IncludeContentChanges": "xx",
                    "Table": "xx",
                    "RecordWithSchema": true
                },
                "Type": "xx",
                "ClsParam": {
                    "LogSet": "xx",
                    "TimeField": "xx",
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

