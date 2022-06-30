**Example 1: 查询表分区**

查询表分区

Input: 

```
tccli dlc DescribeDMSPartitions --cli-unfold-argument  \
    --Name xx \
    --TableName xx \
    --PartValues xx \
    --Values xx \
    --DatabaseName xx \
    --PartitionNames xx \
    --SchemaName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Total": 100,
        "Partitions": [
            {
                "Sds": {
                    "OutputFormat": "xx",
                    "SortCols": {
                        "Col": "xx",
                        "Order": 0
                    },
                    "InputFormat": "xx",
                    "SerdeLib": "xx",
                    "Cols": [
                        {
                            "Name": "xx",
                            "BizParams": [
                                {
                                    "Value": "xx",
                                    "Key": "xx"
                                }
                            ],
                            "IsPartition": true,
                            "Params": [
                                {
                                    "Value": "xx",
                                    "Key": "xx"
                                }
                            ],
                            "Position": 0,
                            "Type": "xx",
                            "Description": "xx"
                        }
                    ],
                    "Compressed": true,
                    "Params": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ],
                    "Location": "xx",
                    "NumBuckets": 0,
                    "SerdeParams": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ],
                    "SerdeName": "xx",
                    "StoredAsSubDirectories": true,
                    "BucketCols": [
                        "xx"
                    ]
                },
                "Name": "xx",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "DataVersion": 0,
                "RecordCount": 0,
                "TableName": "xx",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "Values": [
                    "xx"
                ],
                "DatabaseName": "xx",
                "Params": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "SchemaName": "xx",
                "StorageSize": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

