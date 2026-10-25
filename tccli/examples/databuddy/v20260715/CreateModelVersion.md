**Example 1: 创建模型版本**



Input: 

```
tccli databuddy CreateModelVersion --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ModelName my_model \
    --Uri cos://my-bucket/model/v1 \
    --Comment 模型版本v1 \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Created": true
        }
    }
}
```

