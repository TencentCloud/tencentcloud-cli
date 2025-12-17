**Example 1: DescribeViews示例**



Input: 

```
tccli tccatalog DescribeViews --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName layyu \
    --ViewNames v1
```

Output: 
```
{
    "Response": {
        "Views": [
            {
                "Audit": {
                    "CreatedAt": 1762402442136,
                    "CreatedTime": "2025-11-06 12:14:02",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": 1762402443043,
                    "LastModifiedTime": "2025-11-06 12:14:03",
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
                "EngineType": "spark",
                "Name": "v1",
                "ViewDefinition": "select 1",
                "ViewType": "virtual"
            }
        ],
        "RequestId": "623b2797-292f-4817-872f-13368a78bf73"
    }
}
```

