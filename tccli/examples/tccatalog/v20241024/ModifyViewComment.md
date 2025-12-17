**Example 1: ModifyViewComment示例**



Input: 

```
tccli tccatalog ModifyViewComment --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1 \
    --ViewName v1 \
    --NewComment sfsfe
```

Output: 
```
{
    "Response": {
        "View": {
            "Audit": {
                "CreatedAt": 1760751727724,
                "CreatedTime": "2025-10-18 09:42:07",
                "Creator": "1290245077@qq.com",
                "LastModifiedAt": 1760751749005,
                "LastModifiedTime": "2025-10-18 09:42:29",
                "LastModifier": "1290245077@qq.com"
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
            "Comment": "sfsfe",
            "EngineType": "spark",
            "Name": "v1",
            "ViewDefinition": "select 1",
            "ViewType": "virtual"
        },
        "RequestId": "0a2ff752-f551-498a-a07e-35eb161294ab"
    }
}
```

