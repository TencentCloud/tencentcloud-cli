**Example 1: 创建数据库**



Input: 

```
tccli tccatalog CreateSchema --cli-unfold-argument  \
    --CatalogName test_catalog_001 \
    --Name test_schema_010 \
    --Comment just a test comment \
    --Properties.0.Key testkey \
    --Properties.0.Value testvalue
```

Output: 
```
{
    "Response": {
        "RequestId": "5abcac0a-5342-4090-b3de-771d4e8b602b",
        "Schema": {
            "Audit": {
                "CreatedTime": "2024-12-17 17:31:04",
                "Creator": "100039364093",
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "Comment": "just a test comment",
            "Name": "test_schema_010",
            "Properties": [
                {
                    "Key": "testkey",
                    "Value": "testvalue"
                }
            ]
        }
    }
}
```

