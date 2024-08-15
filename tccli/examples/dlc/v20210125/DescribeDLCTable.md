**Example 1: DLC元数据获取表**



Input: 

```
tccli dlc DescribeDLCTable --cli-unfold-argument  \
    --DbName api_test \
    --Catalog  \
    --Name test \
    --Keyword  \
    --Pattern * \
    --Type  INTERNAL_TABLE
```

Output: 
```
{
    "Response": {
        "DLCTable": {
            "TableBaseInfo": {
                "DatabaseName": "abc",
                "TableName": "abc",
                "DatasourceConnectionName": "abc",
                "TableComment": "abc",
                "Type": "abc",
                "TableFormat": "abc",
                "UserAlias": "abc",
                "UserSubUin": "abc",
                "GovernPolicy": {
                    "RewriteDataPolicy": {
                        "RewriteDataEnable": "abc",
                        "Engine": "abc",
                        "MinInputFiles": 0,
                        "TargetFileSizeBytes": 0,
                        "IntervalMin": 0,
                        "AdvanceParameters": {
                            "CowRewriteEnable": "abc",
                            "RewriteStrategy": "abc",
                            "SortOrders": [
                                {
                                    "Column": "abc",
                                    "SortDirection": "abc",
                                    "NullOrder": "abc"
                                }
                            ]
                        }
                    },
                    "ExpiredSnapshotsPolicy": {
                        "ExpiredSnapshotsEnable": "abc",
                        "Engine": "abc",
                        "RetainLast": 0,
                        "BeforeDays": 0,
                        "MaxConcurrentDeletes": 0,
                        "IntervalMin": 0
                    },
                    "RemoveOrphanFilesPolicy": {
                        "RemoveOrphanFilesEnable": "abc",
                        "Engine": "abc",
                        "BeforeDays": 0,
                        "MaxConcurrentDeletes": 0,
                        "IntervalMin": 0
                    },
                    "MergeManifestsPolicy": {
                        "MergeManifestsEnable": "abc",
                        "Engine": "abc",
                        "IntervalMin": 0
                    },
                    "InheritDataBase": "abc",
                    "RuleType": "abc",
                    "GovernEngine": "abc",
                    "Mode": 0,
                    "PrimaryKeys": "abc"
                },
                "DbGovernPolicyIsDisable": "abc",
                "SmartPolicy": {
                    "BaseInfo": {
                        "Uin": "abc",
                        "PolicyType": "abc",
                        "Catalog": "abc",
                        "Database": "abc",
                        "Table": "abc",
                        "AppId": "abc"
                    },
                    "Policy": {
                        "Inherit": "abc",
                        "Resources": [
                            {
                                "AttributionType": "abc",
                                "ResourceType": "abc",
                                "Name": "abc",
                                "Instance": "abc",
                                "Favor": [
                                    {
                                        "Priority": 0,
                                        "Catalog": "abc",
                                        "DataBase": "abc",
                                        "Table": "abc"
                                    }
                                ],
                                "Status": 0
                            }
                        ],
                        "Written": {
                            "WrittenEnable": "abc",
                            "AdvancePolicy": {
                                "CompactEnable": "abc",
                                "DeleteEnable": "abc",
                                "MinInputFiles": 0,
                                "TargetFileSizeBytes": 0,
                                "RetainLast": 0,
                                "BeforeDays": 0,
                                "ExpiredSnapshotsIntervalMin": 0,
                                "RemoveOrphanIntervalMin": 0,
                                "CowCompactEnable": "abc",
                                "CompactStrategy": "abc",
                                "SortOrders": [
                                    {
                                        "Column": "abc",
                                        "SortDirection": "abc",
                                        "NullOrder": "abc"
                                    }
                                ]
                            }
                        },
                        "Lifecycle": {
                            "LifecycleEnable": "abc",
                            "Expiration": 0,
                            "DropTable": true,
                            "ExpiredField": "abc",
                            "ExpiredFieldFormat": "abc"
                        },
                        "Index": {
                            "IndexEnable": "abc"
                        }
                    }
                }
            },
            "Columns": [
                {
                    "Name": "abc",
                    "Type": "abc",
                    "Comment": "abc",
                    "Default": "abc",
                    "NotNull": true,
                    "Precision": 0,
                    "Scale": 0,
                    "Position": 0,
                    "IsPartition": true
                }
            ],
            "Partitions": [
                {
                    "Name": "abc",
                    "Type": "abc",
                    "Comment": "abc",
                    "PartitionType": "abc",
                    "PartitionFormat": "abc",
                    "PartitionDot": 0,
                    "Transform": "abc",
                    "TransformArgs": [
                        "abc"
                    ]
                }
            ],
            "Location": "abc",
            "Properties": [
                {
                    "Key": "abc",
                    "Value": "abc"
                }
            ],
            "ModifiedTime": "abc",
            "CreateTime": "abc",
            "InputFormat": "abc",
            "StorageSize": 0,
            "RecordCount": 0,
            "MapMaterializedViewName": "abc",
            "HeatValue": 0,
            "ExternalDataConfiguration": {
                "Sds": {
                    "Location": "abc",
                    "InputFormat": "abc",
                    "OutputFormat": "abc",
                    "NumBuckets": 0,
                    "Compressed": true,
                    "StoredAsSubDirectories": true,
                    "SerdeLib": "abc",
                    "SerdeName": "abc",
                    "Params": [],
                    "SerdeParams": [],
                    "SortColumns": [],
                    "BucketCols": [
                        "abc"
                    ],
                    "SortCols": {
                        "Col": "abc",
                        "Order": 0
                    },
                    "Cols": [
                        {
                            "Name": "abc",
                            "Description": "abc",
                            "Type": "abc",
                            "Position": 0,
                            "IsPartition": true
                        }
                    ]
                },
                "ViewOriginalText": "abc",
                "ViewExpandedText": "abc",
                "Retention": 0,
                "LifeTime": 0,
                "Partitions": [
                    {
                        "DatabaseName": "abc",
                        "SchemaName": "abc",
                        "TableName": "abc",
                        "DataVersion": 0,
                        "Name": "abc",
                        "Params": [],
                        "Values": [
                            "abc"
                        ],
                        "StorageSize": 0,
                        "RecordCount": 0,
                        "CreateTime": "2020-09-22T00:00:00+00:00",
                        "ModifiedTime": "2020-09-22T00:00:00+00:00",
                        "LastAccessTime": "2020-09-22T00:00:00+00:00",
                        "Sds": {
                            "Location": "abc",
                            "InputFormat": "abc",
                            "OutputFormat": "abc",
                            "NumBuckets": 0,
                            "Compressed": true,
                            "StoredAsSubDirectories": true,
                            "SerdeLib": "abc",
                            "SerdeName": "abc",
                            "Params": [],
                            "SerdeParams": [],
                            "SortColumns": [],
                            "BucketCols": [
                                "abc"
                            ],
                            "SortCols": {
                                "Col": "abc",
                                "Order": 0
                            },
                            "Cols": [
                                {
                                    "Name": "abc",
                                    "Description": "abc",
                                    "Type": "abc",
                                    "Position": 0,
                                    "IsPartition": true
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "RequestId": "abc"
    }
}
```

