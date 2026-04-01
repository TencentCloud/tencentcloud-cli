**Example 1: 获取table列表**

获取table列表

Input: 

```
tccli wedata ListTables --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Audit": {
                        "CreatedAt": "1761055196090",
                        "Creator": "1290245077@qq.com",
                        "LastModifiedAt": "1761055196633",
                        "LastModifier": "1290245077@qq.com"
                    },
                    "Columns": [
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "order_id_col",
                            "Type": "long"
                        },
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "customer_id_col",
                            "Type": "long"
                        },
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "order_date_col",
                            "Type": "timestamp_tz(6)"
                        },
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "product_id_col",
                            "Type": "integer"
                        },
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "product_name_col",
                            "Type": "string"
                        },
                        {
                            "Comment": "",
                            "FieldSetting": "",
                            "IsPrimaryKey": false,
                            "Name": "quantity_col",
                            "Type": "integer"
                        }
                    ],
                    "Comment": "订单信息托管表（按订单日期分区）",
                    "Indexes": [],
                    "MetaOwner": {
                        "FullName": "DataLakeCatalog.default.order_managed_table",
                        "Owner": "1290245077@qq.com",
                        "OwnerType": "user"
                    },
                    "Name": "order_managed_table",
                    "Partitioning": [
                        {
                            "DayPartitioning": {
                                "FieldName": "order_date_col"
                            },
                            "Strategy": "day"
                        }
                    ],
                    "Properties": [
                        {
                            "Key": "owner",
                            "Value": "root"
                        },
                        {
                            "Key": "write.parquet.compression-codec",
                            "Value": "zstd"
                        },
                        {
                            "Key": "current-snapshot-summary",
                            "Value": "{\"spark.app.id\":\"spark-b4e930acee7a446888167a444b7f292c\",\"added-data-files\":\"1\",\"added-records\":\"1\",\"added-files-size\":\"3246\",\"changed-partition-count\":\"1\",\"total-records\":\"1\",\"total-files-size\":\"3246\",\"total-data-files\":\"1\",\"total-delete-files\":\"0\",\"total-position-deletes\":\"0\",\"total-equality-deletes\":\"0\"}"
                        },
                        {
                            "Key": "write.metadata.delete-after-commit.enabled",
                            "Value": "true"
                        },
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid4204782243991625654"
                        },
                        {
                            "Key": "write.metadata.metrics.default",
                            "Value": "full"
                        },
                        {
                            "Key": "format",
                            "Value": "iceberg/parquet"
                        },
                        {
                            "Key": "format-version",
                            "Value": "2"
                        },
                        {
                            "Key": "uuid",
                            "Value": "2bdf0344-5b4d-4d58-a230-da913481d7fa"
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
                            "Value": "7665350655544053728"
                        },
                        {
                            "Key": "lakehouse.storage.type",
                            "Value": "lakefs"
                        },
                        {
                            "Key": "current-snapshot-timestamp-ms",
                            "Value": "1761055200681"
                        },
                        {
                            "Key": "metadata_location",
                            "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/order_managed_table.1761055194894/metadata/00001-8ed6ace3-fc7e-410d-9dbd-b0e9fc7b984f.metadata.json"
                        },
                        {
                            "Key": "location",
                            "Value": "cosn://dlc4634-700001601851-1740545216-700001779129-251301051/1300298608/warehouse/default.db/order_managed_table.1761055194894"
                        },
                        {
                            "Key": "write.distribution-mode",
                            "Value": "hash"
                        }
                    ],
                    "TableFormat": "订单信息托管表（按订单日期分区）"
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "e74936a8-4226-4bdf-b24d-d1c8484cf410"
    }
}
```

