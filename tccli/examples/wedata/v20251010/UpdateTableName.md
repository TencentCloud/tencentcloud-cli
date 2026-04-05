**Example 1: 重命名表**



Input: 

```
tccli wedata UpdateTableName --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --TableName order_partition_table \
    --NewName order_partition_table_update
```

Output: 
```
{
    "Response": {
        "RequestId": "9ef8e576-a159-4aaa-a275-8ba7992358f7",
        "Data": {
            "Table": {
                "Audit": {
                    "CreatedAt": "1761055227671",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "1761632148347",
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
                        "Name": "payment_method_col",
                        "Type": "string"
                    },
                    {
                        "Comment": "",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "is_paid_col",
                        "Type": "boolean"
                    }
                ],
                "Comment": "订单",
                "Name": "order_partition_table_update",
                "Properties": [
                    {
                        "Key": "engine_version",
                        "Value": "Spark 3.5.3-dlc"
                    }
                ]
            }
        }
    }
}
```

