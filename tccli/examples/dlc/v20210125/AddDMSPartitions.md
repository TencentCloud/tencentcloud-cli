**Example 1: DMS元数据新增分区**



Input: 

```
tccli dlc AddDMSPartitions --cli-unfold-argument  \
    --Partitions.0.Sds.OutputFormat xx \
    --Partitions.0.Sds.SortCols.Col xx \
    --Partitions.0.Sds.SortCols.Order 1 \
    --Partitions.0.Sds.InputFormat xx \
    --Partitions.0.Sds.SerdeLib xx \
    --Partitions.0.Sds.Cols.0.Name xx \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value xx \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key xx \
    --Partitions.0.Sds.Cols.0.IsPartition False \
    --Partitions.0.Sds.Cols.0.Params.0.Value xx \
    --Partitions.0.Sds.Cols.0.Params.0.Key xx \
    --Partitions.0.Sds.Cols.0.Position 1 \
    --Partitions.0.Sds.Cols.0.Type xx \
    --Partitions.0.Sds.Cols.0.Description xx \
    --Partitions.0.Sds.Compressed False \
    --Partitions.0.Sds.Params.0.Value xx \
    --Partitions.0.Sds.Params.0.Key xx \
    --Partitions.0.Sds.Location xx \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value xx \
    --Partitions.0.Sds.SerdeParams.0.Key xx \
    --Partitions.0.Sds.SerdeName xx \
    --Partitions.0.Sds.StoredAsSubDirectories False \
    --Partitions.0.Sds.BucketCols aa bb \
    --Partitions.0.Name xx \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 1 \
    --Partitions.0.RecordCount 1 \
    --Partitions.0.TableName xx \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values 1 2 \
    --Partitions.0.DatabaseName xx \
    --Partitions.0.Params.0.Value xx \
    --Partitions.0.Params.0.Key xx \
    --Partitions.0.SchemaName xx \
    --Partitions.0.StorageSize 1 \
    --Partitions.0.CreateTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "RequestId": "xx",
        "Partitions": [
            {
                "Sds": {
                    "OutputFormat": "xx",
                    "SortCols": {
                        "Col": "xx",
                        "Order": 1
                    },
                    "InputFormat": "xx",
                    "SerdeLib": "xx",
                    "Cols": [
                        {
                            "IsPartition": false,
                            "Type": "xx",
                            "Description": "xx",
                            "Position": 1,
                            "Name": "xx"
                        }
                    ],
                    "Location": "xx",
                    "NumBuckets": 0,
                    "Compressed": false,
                    "SerdeName": "xx",
                    "StoredAsSubDirectories": false,
                    "BucketCols": [
                        "aa",
                        "bb"
                    ]
                },
                "Name": "xx",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "DataVersion": 1,
                "RecordCount": 1,
                "TableName": "xx",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "Values": [
                    "1",
                    "2"
                ],
                "DatabaseName": "xx",
                "SchemaName": "xx",
                "StorageSize": 1,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

