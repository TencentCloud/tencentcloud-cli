**Example 1: 获取数据库详情**



Input: 

```
tccli tccatalog DescribeSchema --cli-unfold-argument  \
    --CatalogName test_catalog_001 \
    --SchemaName test_schema_001
```

Output: 
```
{
    "Response": {
        "RequestId": "cedee360-966d-499c-88e0-53ec1c6a044b",
        "Schema": {
            "Audit": {
                "CreatedTime": "2024-11-26 17:03:56",
                "Creator": "anonymous",
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "Comment": "测试schema_001",
            "Name": "test_schema_001"
        }
    }
}
```

