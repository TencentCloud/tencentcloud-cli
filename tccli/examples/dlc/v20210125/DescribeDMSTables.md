**Example 1: DMS查询表列表**



Input: 

```
tccli dlc DescribeDMSTables --cli-unfold-argument  \
    --Name name1 \
    --Keyword key \
    --Pattern pattern \
    --Catalog hive \
    --SchemaName name \
    --Type t1 \
    --DbName db1 \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "********-********",
        "TableList": [
            {
                "Asset": {
                    "BizParams": [],
                    "Catalog": "hive",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "DataVersion": 0,
                    "DatasourceId": 0,
                    "Description": "",
                    "Guid": "********",
                    "Id": 12345678,
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "Name": "",
                    "Owner": "root",
                    "OwnerAccount": "",
                    "Params": [
                        {
                            "Key": "owner",
                            "Value": "root"
                        },
                        {
                            "Key": "table_type",
                            "Value": "ICEBERG"
                        },
                        {
                            "Key": "totalSize",
                            "Value": "772"
                        },
                        {
                            "Key": "numFiles",
                            "Value": "2"
                        },
                        {
                            "Key": "current-snapshot-id",
                            "Value": "********"
                        },
                        {
                            "Key": "previous_metadata_location",
                            "Value": "cosn://********"
                        },
                        {
                            "Key": "snapshot-count",
                            "Value": "1"
                        },
                        {
                            "Key": "transient_lastDdlTime",
                            "Value": "1739174775725"
                        },
                        {
                            "Key": "EXTERNAL",
                            "Value": "TRUE"
                        },
                        {
                            "Key": "metadata_location",
                            "Value": "cosn://********"
                        },
                        {
                            "Key": "numRows",
                            "Value": "2"
                        },
                        {
                            "Key": "uuid",
                            "Value": "********"
                        },
                        {
                            "Key": "current-snapshot-timestamp-ms",
                            "Value": "1739174803467"
                        },
                        {
                            "Key": "current-snapshot-summary",
                            "Value": "{\"spark.app.id\":\"spark-********\",\"added-data-files\":\"2\",\"added-records\":\"2\",\"added-files-size\":\"772\",\"changed-partition-count\":\"1\",\"total-records\":\"2\",\"total-files-size\":\"772\",\"total-data-files\":\"2\",\"total-delete-files\":\"0\",\"total-position-deletes\":\"0\",\"total-equality-deletes\":\"0\"}"
                        },
                        {
                            "Key": "lakehouse.storage.type",
                            "Value": "lakefs"
                        },
                        {
                            "Key": "write.parquet.compression-codec",
                            "Value": "zstd"
                        },
                        {
                            "Key": "current-schema",
                            "Value": "{\"type\":\"struct\",\"schema-id\":0,\"fields\":[{\"id\":1,\"name\":\"a\",\"required\":false,\"type\":\"int\"}]}"
                        }
                    ],
                    "PermValues": []
                },
                "Table": {
                    "Columns": null,
                    "SchemaName": "",
                    "Retention": 1,
                    "DataUpdateTime": "2020-09-22T00:00:00+00:00",
                    "DbName": "a1",
                    "LastAccessTime": "2020-09-22T00:00:00+00:00",
                    "LifeTime": 0,
                    "Name": "tb1111",
                    "PartitionKeys": [],
                    "Partitions": null,
                    "RecordCount": 2,
                    "Sds": {
                        "BucketCols": null,
                        "Cols": null,
                        "Compressed": false,
                        "InputFormat": "",
                        "Location": "",
                        "NumBuckets": 0,
                        "OutputFormat": "",
                        "Params": null,
                        "SerdeLib": "",
                        "SerdeName": "",
                        "SerdeParams": null,
                        "SortCols": null,
                        "SortColumns": null,
                        "StoredAsSubDirectories": false
                    },
                    "StorageSize": 772,
                    "StructUpdateTime": "2020-09-22T00:00:00+00:00",
                    "Type": "EXTERNAL_TABLE",
                    "ViewExpandedText": "",
                    "ViewOriginalText": ""
                }
            }
        ],
        "TotalCount": 44
    }
}
```

