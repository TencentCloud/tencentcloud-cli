**Example 1: DMS查询表列表**



Input: 

```
tccli dlc DescribeDMSTables --cli-unfold-argument  \
    --Name name1 \
    --Keyword key \
    --Pattern pattern \
    --Catalog DataLakeCatalog \
    --SchemaName name \
    --Type t1 \
    --DbName db1
```

Output: 
```
{
    "Response": {
        "TableList": [
            {
                "Table": {
                    "ViewOriginalText": "abc",
                    "ViewExpandedText": "abc",
                    "Retention": 0,
                    "Columns": [],
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
                                "Params": [
                                    {
                                        "Key": "abc",
                                        "Value": "abc"
                                    }
                                ],
                                "IsPartition": true
                            }
                        ],
                        "SortColumns": [
                            {
                                "Col": "abc",
                                "Order": 0
                            }
                        ]
                    },
                    "PartitionKeys": [
                        {
                            "Name": "abc",
                            "Description": "abc",
                            "Type": "abc",
                            "Position": 0,
                            "IsPartition": true
                        }
                    ],
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
                    ],
                    "Type": "abc",
                    "DbName": "abc",
                    "SchemaName": "abc",
                    "StorageSize": 0,
                    "RecordCount": 0,
                    "LifeTime": 0,
                    "LastAccessTime": "2020-09-22T00:00:00+00:00",
                    "DataUpdateTime": "2020-09-22T00:00:00+00:00",
                    "StructUpdateTime": "2020-09-22T00:00:00+00:00",
                    "Name": "abc"
                },
                "Asset": {
                    "Id": 0,
                    "Name": "abc",
                    "Guid": "abc",
                    "Catalog": "abc",
                    "Description": "abc",
                    "Owner": "abc",
                    "OwnerAccount": "abc",
                    "DataVersion": 0,
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "DatasourceId": 0,
                    "Params": [],
                    "PermValues": [],
                    "BizParams": []
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

