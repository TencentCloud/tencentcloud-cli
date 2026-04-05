**Example 1: 重命名view**

重命名view

Input: 

```
tccli wedata UpdateViewName --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --ViewName order_partition_view \
    --NewName order_partition_view_update
```

Output: 
```
{
    "Response": {
        "RequestId": "9ef8e576-a159-4aaa-a275-8ba7992358f7",
        "Data": {
            "View": {
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
                "Comment": "订单分区视图",
                "Name": "order_partition_view_update",
                "Properties": [
                    {
                        "Key": "create_engine_version",
                        "Value": "Spark 3.5.3-dlc"
                    },
                    {
                        "Key": "comment",
                        "Value": "订单分区视图"
                    },
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

