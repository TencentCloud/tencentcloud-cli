**Example 1: DMS元数据新增分区**



Input: 

```
tccli dlc AddDMSPartitions --cli-unfold-argument  \
    --Partitions.0.Sds.OutputFormat org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat \
    --Partitions.0.Sds.SortCols.Col col1 \
    --Partitions.0.Sds.SortCols.Order 1 \
    --Partitions.0.Sds.InputFormat org.apache.hadoop.mapred.TextInputFormat \
    --Partitions.0.Sds.SerdeLib org.apache.hadoop.hive.serde2.OpenCSVSerde \
    --Partitions.0.Sds.Cols.0.Name col1 \
    --Partitions.0.Sds.Cols.0.BizParams.0.Key biz-param-key \
    --Partitions.0.Sds.Cols.0.BizParams.0.Value biz-param-value \
    --Partitions.0.Sds.Cols.0.IsPartition False \
    --Partitions.0.Sds.Cols.0.Params.0.Key para1 \
    --Partitions.0.Sds.Cols.0.Params.0.Value value1 \
    --Partitions.0.Sds.Cols.0.Position 1 \
    --Partitions.0.Sds.Cols.0.Type string \
    --Partitions.0.Sds.Cols.0.Description description \
    --Partitions.0.Sds.Compressed False \
    --Partitions.0.Sds.Params.0.Key param-key \
    --Partitions.0.Sds.Params.0.Value param-value \
    --Partitions.0.Sds.Location cosn://bucket-name/path-to-local \
    --Partitions.0.Sds.NumBuckets 0 \
    --Partitions.0.Sds.SerdeParams.0.Value serialization.format \
    --Partitions.0.Sds.SerdeParams.0.Key 1 \
    --Partitions.0.Sds.SerdeName serdeName \
    --Partitions.0.Sds.StoredAsSubDirectories False \
    --Partitions.0.Sds.BucketCols col1 \
    --Partitions.0.Name table1 \
    --Partitions.0.ModifiedTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.DataVersion 1 \
    --Partitions.0.RecordCount 1 \
    --Partitions.0.TableName table1 \
    --Partitions.0.LastAccessTime 2020-09-22T00:00:00+00:00 \
    --Partitions.0.Values dt=20220101 \
    --Partitions.0.DatabaseName database1 \
    --Partitions.0.Params.0.Key param-key \
    --Partitions.0.Params.0.Value param-value \
    --Partitions.0.SchemaName database1 \
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
                "DatabaseName": "database1",
                "SchemaName": "database1",
                "TableName": "table1",
                "DataVersion": 0,
                "Name": "20220101",
                "Values": [
                    "dt=20220101"
                ],
                "StorageSize": 0,
                "RecordCount": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "Params": [
                    {
                        "Key": "para-key",
                        "Value": "para-value"
                    }
                ],
                "Sds": {
                    "Location": "cosn://bucket-name/path-to-local",
                    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                    "NumBuckets": 0,
                    "Compressed": true,
                    "StoredAsSubDirectories": true,
                    "SerdeLib": "org.apache.hadoop.hive.serde2.OpenCSVSerde",
                    "SerdeName": "",
                    "BucketCols": [],
                    "SerdeParams": [
                        {
                            "Key": "serialization.format",
                            "Value": "\""
                        }
                    ],
                    "Params": [
                        {
                            "Key": "param-key1",
                            "Value": "param-value1"
                        }
                    ],
                    "SortCols": {
                        "Col": "col1",
                        "Order": 0
                    },
                    "Cols": [
                        {
                            "Name": "col1",
                            "Description": "",
                            "Type": "string",
                            "Position": 0,
                            "IsPartition": true,
                            "BizParams": [],
                            "Params": []
                        }
                    ],
                    "SortColumns": []
                }
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

