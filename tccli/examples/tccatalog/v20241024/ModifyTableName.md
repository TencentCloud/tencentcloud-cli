**Example 1: ModifyTableName示例**



Input: 

```
tccli tccatalog ModifyTableName --cli-unfold-argument  \
    --CatalogName pycatalog \
    --SchemaName pyschema \
    --TableName py_table \
    --NewName py_table_new
```

Output: 
```
{
    "Response": {
        "Table": {
            "Audit": {
                "CreatedAt": 1760945961030,
                "CreatedTime": "2025-10-20 15:39:21",
                "Creator": "tccatalogK5@rZl.com",
                "LastModifiedAt": 1760955788091,
                "LastModifiedTime": "2025-10-20 18:23:08",
                "LastModifier": "tccatalogK5@rZl.com"
            },
            "Columns": [
                {
                    "Comment": "u4e3bu952e",
                    "FieldSetting": "",
                    "IsPrimaryKey": false,
                    "Name": "id",
                    "Type": "integer"
                }
            ],
            "Comment": "u7528u4e8eViewu6d4bu8bd5u7684u8868",
            "Name": "py_table_new",
            "Properties": [
                {
                    "Key": "write.metadata.delete-after-commit.enabled",
                    "Value": "true"
                }
            ],
            "TableFormat": "u7528u4e8eViewu6d4bu8bd5u7684u8868"
        },
        "RequestId": "65595325-0d44-43e3-b021-be5f4e810e3c"
    }
}
```

