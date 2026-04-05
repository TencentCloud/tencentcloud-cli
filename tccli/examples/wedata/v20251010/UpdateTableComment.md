**Example 1: 更新table描述**

更新table描述

Input: 

```
tccli wedata UpdateTableComment --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --TableName modify_1024_05 \
    --NewComment update comment
```

Output: 
```
{
    "Response": {
        "RequestId": "517ad9c9-53d3-4406-85f2-642dce229296",
        "Data": {
            "Table": {
                "Audit": {
                    "CreatedAt": "0",
                    "Creator": "",
                    "LastModifiedAt": "1761631700395",
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
                "Comment": "update comment",
                "Indexes": [],
                "Name": "modify_1024_05",
                "Partitioning": [],
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4284773195429403503"
                    },
                    {
                        "Key": "format",
                        "Value": "iceberg/parquet"
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
                        "Key": "current-snapshot-id",
                        "Value": "none"
                    },
                    {
                        "Key": "write.parquet.compression-codec",
                        "Value": "zstd"
                    },
                    {
                        "Key": "write.upsert.enabled",
                        "Value": "false"
                    },
                    {
                        "Key": "location",
                        "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/myquser.1760698472074"
                    },
                    {
                        "Key": "",
                        "Value": ""
                    },
                    {
                        "Key": "format-version",
                        "Value": "1"
                    },
                    {
                        "Key": "write.metadata.delete-after-commit.enabled",
                        "Value": "true"
                    },
                    {
                        "Key": "write.metadata.metrics.default",
                        "Value": "full"
                    },
                    {
                        "Key": "uuid",
                        "Value": "2e8b0aa3-d253-4a04-bc57-9376ac9c1d84"
                    },
                    {
                        "Key": "metadata_location",
                        "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/myquser.1760698472074/metadata/00001-43bac03f-166e-4155-9732-ac341a1c200d.metadata.json"
                    },
                    {
                        "Key": "write.distribution-mode",
                        "Value": "none"
                    }
                ],
                "TableFormat": "update comment"
            }
        }
    }
}
```

