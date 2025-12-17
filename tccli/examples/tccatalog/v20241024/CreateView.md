**Example 1: CreateView示例**



Input: 

```
tccli tccatalog CreateView --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName layyu \
    --ViewName v1 \
    --ViewType VIRTUAL \
    --EngineType SPARK \
    --ViewDefinition select 1 \
    --Columns.0.Name c1 \
    --Columns.0.Type integer
```

Output: 
```
{
    "Response": {
        "View": {
            "Audit": {
                "CreatedAt": 1762402442136,
                "CreatedTime": "2025-11-06 12:14:02",
                "Creator": "1290245077@qq.com",
                "LastModifiedAt": null,
                "LastModifiedTime": "",
                "LastModifier": ""
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
            "EngineType": "spark",
            "Name": "v1",
            "ViewDefinition": "select 1",
            "ViewType": "virtual"
        },
        "RequestId": "83756ea1-0652-423d-b9af-c54057e218a1"
    }
}
```

