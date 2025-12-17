**Example 1: 获取test_catalog_001下所有数据库名**



Input: 

```
tccli tccatalog DescribeSchemaNames --cli-unfold-argument  \
    --CatalogName test_catalog_001
```

Output: 
```
{
    "Response": {
        "RequestId": "e6f4a5e2-5a55-40ad-8354-b786a950ae61",
        "SchemaNames": [
            {
                "Name": "test_schema_001",
                "Namespace": [
                    "default",
                    "test_catalog_001"
                ]
            }
        ]
    }
}
```

