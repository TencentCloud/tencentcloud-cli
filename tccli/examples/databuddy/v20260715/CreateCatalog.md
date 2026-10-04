**Example 1: 创建数据目录**



Input: 

```
tccli databuddy CreateCatalog --cli-unfold-argument  \
    --Name my_catalog \
    --Type TABLE \
    --WorkspaceId 17697667906247629 \
    --Comment 这是一个数据目录
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "CatalogId": "e3f9a474-0f2e-4f93-90e7-b2fc9ec1405c"
        }
    }
}
```

