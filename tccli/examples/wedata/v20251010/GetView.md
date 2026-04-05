**Example 1: 查询view详情**



Input: 

```
tccli wedata GetView --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --ViewName order_partition_view
```

Output: 
```
{
    "Response": {
        "RequestId": "b5a9e27a-358e-45f1-89c5-c56ce24d10df",
        "Data": {
            "View": {
                "Audit": {
                    "CreatedAt": "1761055227671",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "0",
                    "LastModifier": ""
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
                        "Name": "quantity_col",
                        "Type": "integer"
                    }
                ],
                "Comment": "订单分区视图",
                "MetaOwner": {
                    "FullName": "DataLakeCatalog.default.order_partition_view",
                    "Owner": "1290245077@qq.com",
                    "OwnerType": "user"
                },
                "Name": "order_partition_view",
                "Properties": [
                    {
                        "Key": "comment",
                        "Value": "订单分区视图"
                    },
                    {
                        "Key": "create_engine_version",
                        "Value": "Spark 3.5.3-dlc"
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

