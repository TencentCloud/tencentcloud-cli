**Example 1: DMS查询表列表**



Input: 

```
tccli dlc DescribeDMSTables --cli-unfold-argument  \
    --Name xx \
    --Keyword xx \
    --Pattern xx \
    --Catalog xx \
    --SchemaName xx \
    --Type xx \
    --DbName xx
```

Output: 
```
{
    "Response": {
        "TableList": [
            {
                "Table": {
                    "PartitionKeys": [
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
                                "Position": 0,
                                "Type": "xx",
                                "Description": "xx"
                            }
                        ],
                        "Location": "xx",
                        "NumBuckets": 0,
                        "Compressed": true,
                        "SerdeName": "xx",
                        "StoredAsSubDirectories": true,
                        "BucketCols": [
                            "xx"
                        ]
                    },
                    "RecordCount": 0,
                    "StructUpdateTime": "2020-09-22T00:00:00+00:00",
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
                                        "IsPartition": true,
                                        "Type": "xx",
                                        "Description": "xx",
                                        "Position": 0,
                                        "Name": "xx"
                                    }
                                ],
                                "Location": "xx",
                                "NumBuckets": 0,
                                "Compressed": true,
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
                            "SchemaName": "xx",
                            "StorageSize": 0,
                            "CreateTime": "2020-09-22T00:00:00+00:00"
                        }
                    ],
                    "DataUpdateTime": "2020-09-22T00:00:00+00:00",
                    "ViewOriginalText": "xx",
                    "LifeTime": 0,
                    "StorageSize": 0,
                    "ViewExpandedText": "xx",
                    "SchemaName": "xx",
                    "LastAccessTime": "2020-09-22T00:00:00+00:00",
                    "Type": "xx",
                    "DbName": "xx",
                    "Retention": 0
                },
                "Asset": {
                    "Description": "xx",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "DataVersion": 0,
                    "OwnerAccount": "xx",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "Catalog": "xx",
                    "DatasourceId": 0,
                    "Owner": "xx",
                    "Guid": "xx",
                    "Id": 0,
                    "Name": "xx"
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

