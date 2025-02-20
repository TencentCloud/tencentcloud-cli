**Example 1: 查询表分区**

查询表分区

Input: 

```
tccli dlc DescribeDMSPartitions --cli-unfold-argument  \
    --Name partition1 \
    --TableName table1 \
    --PartValues 1 \
    --Values 1 \
    --DatabaseName database1 \
    --PartitionNames partition1 \
    --SchemaName schema1 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Partitions": [
            {
                "DatabaseName": "database1",
                "SchemaName": "schema1",
                "TableName": "table1",
                "DataVersion": 0,
                "Name": "partition1",
                "Values": [
                    "1"
                ],
                "StorageSize": 0,
                "RecordCount": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "Params": [
                    {
                        "Key": "param1",
                        "Value": "default"
                    }
                ],
                "Sds": {
                    "Location": "cosn://*******",
                    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat",
                    "NumBuckets": 0,
                    "Compressed": true,
                    "StoredAsSubDirectories": true,
                    "SerdeLib": "org.apache.hadoop.hive.serde2.OpenCSVSerde",
                    "SerdeName": "serdename",
                    "BucketCols": [
                        "column1"
                    ],
                    "SerdeParams": [
                        {
                            "Key": "serde param",
                            "Value": "default"
                        }
                    ],
                    "Params": [
                        {
                            "Key": "param1",
                            "Value": "default"
                        }
                    ],
                    "SortCols": {
                        "Col": "column1",
                        "Order": 0
                    },
                    "Cols": [
                        {
                            "Name": "column1",
                            "Description": "default description",
                            "Type": "int",
                            "Position": 0,
                            "IsPartition": true,
                            "BizParams": [],
                            "Params": []
                        }
                    ],
                    "SortColumns": [
                        {
                            "Col": "column1",
                            "Order": 0
                        }
                    ]
                }
            }
        ],
        "Total": 1,
        "RequestId": "*******-********"
    }
}
```

