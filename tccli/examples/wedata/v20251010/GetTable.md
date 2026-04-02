**Example 1: 获取table详情**

获取table详情

Input: 

```
tccli wedata GetTable --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --TableName modify_1024_05
```

Output: 
```
{
    "Response": {
        "RequestId": "43e5f86e-235b-4902-9914-5c2fbba39373",
        "Data": {
            "Table": {
                "Audit": {
                    "CreatedAt": "0",
                    "Creator": "",
                    "LastModifiedAt": "1761300621782",
                    "LastModifier": "1290245077@qq.com"
                },
                "Columns": [
                    {
                        "Comment": "id",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "id",
                        "Type": "string"
                    }
                ],
                "Comment": "qw",
                "Indexes": [],
                "Name": "modify_1024_05",
                "Partitioning": [],
                "Properties": [
                    {
                        "Key": "write.parquet.compression-codec",
                        "Value": "zstd"
                    },
                    {
                        "Key": "format-version",
                        "Value": "1"
                    },
                    {
                        "Key": "provider",
                        "Value": "iceberg"
                    },
                    {
                        "Key": "write.metadata.previous-versions-max",
                        "Value": "100"
                    },
                    {
                        "Key": "metadata_location",
                        "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/myquser.1760698472074/metadata/00000-c09780b5-0893-40b1-9531-8332be94db68.metadata.json"
                    },
                    {
                        "Key": "",
                        "Value": ""
                    },
                    {
                        "Key": "write.upsert.enabled",
                        "Value": "false"
                    },
                    {
                        "Key": "format",
                        "Value": "iceberg/parquet"
                    },
                    {
                        "Key": "uuid",
                        "Value": "2e8b0aa3-d253-4a04-bc57-9376ac9c1d84"
                    },
                    {
                        "Key": "current-snapshot-id",
                        "Value": "none"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4284773195429403503"
                    },
                    {
                        "Key": "write.distribution-mode",
                        "Value": "none"
                    },
                    {
                        "Key": "write.metadata.delete-after-commit.enabled",
                        "Value": "true"
                    },
                    {
                        "Key": "write.metadata.metrics.default",
                        "Value": "full"
                    }
                ],
                "TableFormat": ""
            }
        }
    }
}
```

