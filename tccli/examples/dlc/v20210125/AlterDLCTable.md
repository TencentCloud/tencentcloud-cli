**Example 1: DLC元数据更新表**



Input: 

```
tccli dlc AlterDLCTable --cli-unfold-argument  \
    --CurrentDatabaseName abc \
    --CurrentName abc \
    --TableBaseInfo.DatabaseName abc \
    --TableBaseInfo.TableName abc \
    --TableBaseInfo.DatasourceConnectionName abc \
    --TableBaseInfo.TableComment abc \
    --TableBaseInfo.Type abc \
    --TableBaseInfo.TableFormat abc \
    --TableBaseInfo.UserAlias abc \
    --TableBaseInfo.UserSubUin abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.RewriteDataEnable abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.MinInputFiles 0 \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.TargetFileSizeBytes 0 \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.AdvanceParameters.CowRewriteEnable abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.AdvanceParameters.RewriteStrategy abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.AdvanceParameters.SortOrders.0.Column abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.AdvanceParameters.SortOrders.0.SortDirection abc \
    --TableBaseInfo.GovernPolicy.RewriteDataPolicy.AdvanceParameters.SortOrders.0.NullOrder abc \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.ExpiredSnapshotsEnable abc \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.RetainLast 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.BeforeDays 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.MaxConcurrentDeletes 0 \
    --TableBaseInfo.GovernPolicy.ExpiredSnapshotsPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.RemoveOrphanFilesEnable abc \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.BeforeDays 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.MaxConcurrentDeletes 0 \
    --TableBaseInfo.GovernPolicy.RemoveOrphanFilesPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.MergeManifestsEnable abc \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.Engine abc \
    --TableBaseInfo.GovernPolicy.MergeManifestsPolicy.IntervalMin 0 \
    --TableBaseInfo.GovernPolicy.InheritDataBase abc \
    --TableBaseInfo.GovernPolicy.RuleType abc \
    --TableBaseInfo.GovernPolicy.GovernEngine abc \
    --TableBaseInfo.GovernPolicy.Mode 0 \
    --TableBaseInfo.GovernPolicy.PrimaryKeys abc \
    --TableBaseInfo.DbGovernPolicyIsDisable abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Uin abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.PolicyType abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Catalog abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Database abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.Table abc \
    --TableBaseInfo.SmartPolicy.BaseInfo.AppId abc \
    --TableBaseInfo.SmartPolicy.Policy.Inherit abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.AttributionType abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.ResourceType abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Name abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Instance abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Priority 0 \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Catalog abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.DataBase abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Favor.0.Table abc \
    --TableBaseInfo.SmartPolicy.Policy.Resources.0.Status 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.WrittenEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CompactEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.DeleteEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.MinInputFiles 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.TargetFileSizeBytes 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RetainLast 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.BeforeDays 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.ExpiredSnapshotsIntervalMin 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.RemoveOrphanIntervalMin 0 \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CowCompactEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.CompactStrategy abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.SortOrders.0.Column abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.SortOrders.0.SortDirection abc \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.SortOrders.0.NullOrder abc \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.LifecycleEnable abc \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.Expiration 0 \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.DropTable True \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredField abc \
    --TableBaseInfo.SmartPolicy.Policy.Lifecycle.ExpiredFieldFormat abc \
    --TableBaseInfo.SmartPolicy.Policy.Index.IndexEnable abc \
    --TableType abc \
    --Columns.Name abc \
    --Columns.Type abc \
    --Columns.Comment abc \
    --Columns.Default abc \
    --Columns.NotNull True \
    --Columns.Precision 0 \
    --Columns.Scale 0 \
    --Columns.Position 0 \
    --Columns.IsPartition True \
    --Partitions.Name abc \
    --Partitions.Type abc \
    --Partitions.Comment abc \
    --Partitions.PartitionType abc \
    --Partitions.PartitionFormat abc \
    --Partitions.PartitionDot 0 \
    --Partitions.Transform abc \
    --Partitions.TransformArgs abc \
    --Properties.Key abc \
    --Properties.Value abc \
    --ExternalDataConfiguration.Sds.Location abc \
    --ExternalDataConfiguration.Sds.InputFormat abc \
    --ExternalDataConfiguration.Sds.OutputFormat abc \
    --ExternalDataConfiguration.Sds.NumBuckets 0 \
    --ExternalDataConfiguration.Sds.Compressed True \
    --ExternalDataConfiguration.Sds.StoredAsSubDirectories True \
    --ExternalDataConfiguration.Sds.SerdeLib abc \
    --ExternalDataConfiguration.Sds.SerdeName abc \
    --ExternalDataConfiguration.Sds.BucketCols abc \
    --ExternalDataConfiguration.Sds.SerdeParams.0.Key abc \
    --ExternalDataConfiguration.Sds.SerdeParams.0.Value abc \
    --ExternalDataConfiguration.Sds.Params.0.Key abc \
    --ExternalDataConfiguration.Sds.Params.0.Value abc \
    --ExternalDataConfiguration.Sds.SortCols.Col abc \
    --ExternalDataConfiguration.Sds.SortCols.Order 0 \
    --ExternalDataConfiguration.Sds.Cols.0.Name abc \
    --ExternalDataConfiguration.Sds.Cols.0.Description abc \
    --ExternalDataConfiguration.Sds.Cols.0.Type abc \
    --ExternalDataConfiguration.Sds.Cols.0.Position 0 \
    --ExternalDataConfiguration.Sds.Cols.0.Params.0.Key abc \
    --ExternalDataConfiguration.Sds.Cols.0.Params.0.Value abc \
    --ExternalDataConfiguration.Sds.Cols.0.IsPartition True \
    --ExternalDataConfiguration.Sds.SortColumns.0.Col abc \
    --ExternalDataConfiguration.Sds.SortColumns.0.Order 0 \
    --ExternalDataConfiguration.ViewOriginalText abc \
    --ExternalDataConfiguration.ViewExpandedText abc \
    --ExternalDataConfiguration.Retention 0 \
    --ExternalDataConfiguration.LifeTime 0 \
    --ExternalDataConfiguration.Partitions.0.DatabaseName abc \
    --ExternalDataConfiguration.Partitions.0.SchemaName abc \
    --ExternalDataConfiguration.Partitions.0.TableName abc \
    --ExternalDataConfiguration.Partitions.0.DataVersion 0 \
    --ExternalDataConfiguration.Partitions.0.Name abc \
    --ExternalDataConfiguration.Partitions.0.Values abc \
    --ExternalDataConfiguration.Partitions.0.StorageSize 0 \
    --ExternalDataConfiguration.Partitions.0.RecordCount 0 \
    --ExternalDataConfiguration.Partitions.0.CreateTime 2020-09-22T00:00:00+00:00 \
    --ExternalDataConfiguration.Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --ExternalDataConfiguration.Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --ExternalDataConfiguration.Partitions.0.Sds.Location abc \
    --ExternalDataConfiguration.Partitions.0.Sds.InputFormat abc \
    --ExternalDataConfiguration.Partitions.0.Sds.OutputFormat abc \
    --ExternalDataConfiguration.Partitions.0.Sds.NumBuckets 0 \
    --ExternalDataConfiguration.Partitions.0.Sds.Compressed True \
    --ExternalDataConfiguration.Partitions.0.Sds.StoredAsSubDirectories True \
    --ExternalDataConfiguration.Partitions.0.Sds.SerdeLib abc \
    --ExternalDataConfiguration.Partitions.0.Sds.SerdeName abc \
    --ExternalDataConfiguration.Partitions.0.Sds.BucketCols abc \
    --ExternalDataConfiguration.Partitions.0.Sds.SortCols.Col abc \
    --ExternalDataConfiguration.Partitions.0.Sds.SortCols.Order 0 \
    --ExternalDataConfiguration.Partitions.0.Sds.Cols.0.Name abc \
    --ExternalDataConfiguration.Partitions.0.Sds.Cols.0.Description abc \
    --ExternalDataConfiguration.Partitions.0.Sds.Cols.0.Type abc \
    --ExternalDataConfiguration.Partitions.0.Sds.Cols.0.Position 0 \
    --ExternalDataConfiguration.Partitions.0.Sds.Cols.0.IsPartition True \
    --DataEngineName abc \
    --ResourceGroupName abc
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
        "Execution": "alter table `table1` rename to `table2`",
        "RequestId": "abc"
    }
}
```

