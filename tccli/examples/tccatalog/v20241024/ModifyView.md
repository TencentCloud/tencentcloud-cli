**Example 1: ModifyView示例**



Input: 

```
tccli tccatalog ModifyView --cli-unfold-argument  \
    --CatalogName layyu_c4 \
    --SchemaName s1 \
    --ViewName v2 \
    --NewName v3 \
    --NewComment this is test view
```

Output: 
```
{
    "Response": {
        "View": {
            "Audit": {
                "CreatedAt": 1762485462377,
                "CreatedTime": "2025-11-07 11:17:42",
                "Creator": "tccatalogK5@rZl.com",
                "LastModifiedAt": 1762485502338,
                "LastModifiedTime": "2025-11-07 11:18:22",
                "LastModifier": "tccatalogK5@rZl.com"
            },
            "Columns": [
                {
                    "Comment": "",
                    "FieldSetting": "",
                    "IsPrimaryKey": false,
                    "Name": "c1",
                    "Type": "integer"
                }
            ],
            "Comment": "this is test view",
            "EngineType": "spark",
            "Name": "v3",
            "Properties": [
                {
                    "Key": "k1",
                    "Value": "v1"
                }
            ],
            "ViewDefinition": "select 1",
            "ViewType": "virtual"
        },
        "RequestId": "c1462171-d5c0-4327-818a-0d0a4c888947"
    }
}
```

