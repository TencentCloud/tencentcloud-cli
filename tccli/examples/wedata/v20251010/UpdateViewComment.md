**Example 1: 更新view描述**

更新view描述

Input: 

```
tccli wedata UpdateViewComment --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --ViewName order_partition_view \
    --NewComment update comment
```

Output: 
```
{
    "Response": {
        "RequestId": "5bc99ce6-ff0d-466b-b680-6d90dfd3c3c2",
        "Data": {
            "View": {
                "Audit": {
                    "CreatedAt": "1761055227671",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "1761632207782",
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
                        "Name": "is_paid_col",
                        "Type": "boolean"
                    }
                ],
                "Comment": "update comment",
                "Name": "order_partition_view",
                "Properties": [
                    {
                        "Key": "comment",
                        "Value": "订单分区视图"
                    },
                    {
                        "Key": "engine_version",
                        "Value": "Spark 3.5.3-dlc"
                    },
                    {
                        "Key": "create_engine_version",
                        "Value": "Spark 3.5.3-dlc"
                    }
                ]
            }
        }
    }
}
```

