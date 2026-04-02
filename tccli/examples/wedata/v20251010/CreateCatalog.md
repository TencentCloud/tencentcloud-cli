**Example 1: 创建数据目录**

创建数据目录

Input: 

```
tccli wedata CreateCatalog --cli-unfold-argument  \
    --Name mico_catalog_1025 \
    --Type TABLE \
    --WorkspaceId default \
    --Comment test create
```

Output: 
```
{
    "Response": {
        "Data": {
            "CatalogId": "9282d7bd-9fde-4ec1-bd8f-c0096146095b"
        },
        "RequestId": "ef2c4e2b-8795-407e-902a-aae86b620b86"
    }
}
```

