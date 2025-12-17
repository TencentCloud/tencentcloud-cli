**Example 1: ModifyTableColumnComment示例**



Input: 

```
tccli tccatalog ModifyTableColumnComment --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1 \
    --TableName t2 \
    --FieldName c1 \
    --NewComment this is c1
```

Output: 
```
{
    "Response": {
        "Table": {
            "Audit": {
                "CreatedAt": 1761199595810,
                "CreatedTime": "2025-10-23 14:06:35",
                "Creator": "tccatalogK5@rZl.com",
                "LastModifiedAt": 1762485793648,
                "LastModifiedTime": "2025-11-07 11:23:13",
                "LastModifier": "tccatalogK5@rZl.com"
            },
            "Columns": [
                {
                    "Comment": "",
                    "FieldSetting": "",
                    "IsPrimaryKey": false,
                    "Name": "c3",
                    "Type": "string"
                }
            ],
            "Comment": "",
            "FormatType": "",
            "Name": "t2",
            "Properties": [
                {
                    "Key": "current-snapshot-id",
                    "Value": "none"
                }
            ],
            "TableFormat": ""
        },
        "RequestId": "5cb44a00-2bb3-473c-9fec-98e416cad911"
    }
}
```

