**Example 1: 查询表分区**

查询表分区

Input: 

```
tccli dlc DescribeDMSPartitions --cli-unfold-argument  \
    --Name abc \
    --TableName abc \
    --PartValues abc \
    --Values abc \
    --DatabaseName abc \
    --PartitionNames abc \
    --SchemaName abc
```

Output: 
```
{
    "Response": {
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
        "Total": 0,
        "RequestId": "abc"
    }
}
```

