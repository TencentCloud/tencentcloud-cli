**Example 1: 查询表**



Input: 

```
tccli dlc DescribeDMSTable --cli-unfold-argument  \
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
        "Type": "xx",
        "RecordCount": 0,
        "StructUpdateTime": "2020-09-22T00:00:00+00:00",
        "DataUpdateTime": "2020-09-22T00:00:00+00:00",
        "ViewOriginalText": "xx",
        "LifeTime": 0,
        "RequestId": "xx",
        "Retention": 0,
        "Asset": {
            "Description": "xx",
            "ModifiedTime": "2020-09-22T00:00:00+00:00",
            "DataVersion": 0,
            "BizParams": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "OwnerAccount": "xx",
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "Catalog": "xx",
            "Params": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "PermValues": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "Owner": "xx",
            "DatasourceId": 0,
            "Guid": "xx",
            "Id": 0,
            "Name": "xx"
        },
        "ViewExpandedText": "xx",
        "SchemaName": "xx",
        "LastAccessTime": "2020-09-22T00:00:00+00:00",
        "StorageSize": 0,
        "DbName": "xx",
        "Columns": [
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

