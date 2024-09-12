**Example 1: DMS元数据新增分区**



Input: 

```
tccli dlc AddDMSPartitions --cli-unfold-argument  \
    --Partitions.0.Sds.OutputFormat abc \
    --Partitions.0.Sds.SortCols.Col abc \
    --Partitions.0.Sds.SortCols.Order 1 \
    --Partitions.0.Sds.InputFormat abc \
    --Partitions.0.Sds.SerdeLib abc \
    --Partitions.0.Sds.Cols.0.Name abc \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value abc \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key abc \
    --Partitions.0.Sds.Cols.0.IsPartition False \
    --Partitions.0.Sds.Cols.0.Params.0.Value abc \
    --Partitions.0.Sds.Cols.0.Params.0.Key abc \
    --Partitions.0.Sds.Cols.0.Position 1 \
    --Partitions.0.Sds.Cols.0.Type abc \
    --Partitions.0.Sds.Cols.0.Description abc \
    --Partitions.0.Sds.Compressed False \
    --Partitions.0.Sds.Params.0.Value abc \
    --Partitions.0.Sds.Params.0.Key abc \
    --Partitions.0.Sds.Location abc \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value abc \
    --Partitions.0.Sds.SerdeParams.0.Key abc \
    --Partitions.0.Sds.SerdeName abc \
    --Partitions.0.Sds.StoredAsSubDirectories False \
    --Partitions.0.Sds.BucketCols aa bb \
    --Partitions.0.Name abc \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 1 \
    --Partitions.0.RecordCount 1 \
    --Partitions.0.TableName abc \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values 1 2 \
    --Partitions.0.DatabaseName abc \
    --Partitions.0.Params.0.Value abc \
    --Partitions.0.Params.0.Key abc \
    --Partitions.0.SchemaName abc \
    --Partitions.0.StorageSize 1 \
    --Partitions.0.CreateTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Partitions": [
            {
                "DatabaseName": "abc",
                "SchemaName": "abc",
                "TableName": "abc",
                "DataVersion": 0,
                "Name": "abc",
                "Values": [
                    "abc"
                ],
                "StorageSize": 0,
                "RecordCount": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "Params": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Sds": {
                    "Location": "abc",
                    "InputFormat": "abc",
                    "OutputFormat": "abc",
                    "NumBuckets": 0,
                    "Compressed": true,
                    "StoredAsSubDirectories": true,
                    "SerdeLib": "abc",
                    "SerdeName": "abc",
                    "BucketCols": [
                        "abc"
                    ],
                    "SerdeParams": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
                    ],
                    "Params": [
                        {
                            "Key": "abc",
                            "Value": "abc"
                        }
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
                            "IsPartition": true,
                            "BizParams": [],
                            "Params": []
                        }
                    ],
                    "SortColumns": [
                        {
                            "Col": "abc",
                            "Order": 0
                        }
                    ]
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

