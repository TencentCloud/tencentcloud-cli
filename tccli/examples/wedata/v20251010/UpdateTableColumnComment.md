**Example 1: 更新表字段描述**

更新表字段描述

Input: 

```
tccli wedata UpdateTableColumnComment --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --TableName modify_1024_05_update \
    --NewComment update column commen agagin \
    --FieldName id
```

Output: 
```
{
    "Response": {
        "RequestId": "8bce9cc7-4140-48ce-aa57-a8ad5fb7b22f",
        "Data": {
            "Table": {
                "Audit": {
                    "CreatedAt": "0",
                    "Creator": "",
                    "LastModifiedAt": "1761749188892",
                    "LastModifier": "1290245077@qq.com"
                },
                "Columns": [
                    {
                        "Comment": "update column commen agagin",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "id",
                        "Type": "string"
                    }
                ],
                "Comment": "update comment",
                "Indexes": [],
                "Name": "modify_1024_05_update",
                "Partitioning": [],
                "Properties": [
                    {
                        "Key": "write.parquet.compression-codec",
                        "Value": "zstd"
                    },
                    {
                        "Key": "write.upsert.enabled",
                        "Value": "false"
                    },
                    {
                        "Key": "write.metadata.previous-versions-max",
                        "Value": "100"
                    },
                    {
                        "Key": "write.distribution-mode",
                        "Value": "none"
                    },
                    {
                        "Key": "write.metadata.metrics.default",
                        "Value": "full"
                    },
                    {
                        "Key": "current-snapshot-id",
                        "Value": "none"
                    },
                    {
                        "Key": "location",
                        "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/myquser.1760698472074"
                    },
                    {
                        "Key": "write.metadata.delete-after-commit.enabled",
                        "Value": "true"
                    },
                    {
                        "Key": "uuid",
                        "Value": "2e8b0aa3-d253-4a04-bc57-9376ac9c1d84"
                    },
                    {
                        "Key": "provider",
                        "Value": "iceberg"
                    },
                    {
                        "Key": "metadata_location",
                        "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/myquser.1760698472074/metadata/00003-5faa47df-8d50-44d9-ac9c-7bf424220f9b.metadata.json"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4284773195429403503"
                    },
                    {
                        "Key": "",
                        "Value": ""
                    },
                    {
                        "Key": "format",
                        "Value": "iceberg/parquet"
                    },
                    {
                        "Key": "format-version",
                        "Value": "1"
                    }
                ],
                "TableFormat": "update comment"
            }
        }
    }
}
```

