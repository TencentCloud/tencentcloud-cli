**Example 1: 创建模型**



Input: 

```
tccli databuddy CreateModel --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ModelName my_model \
    --WorkspaceId 17697667906247629 \
    --Comment 这是一个模型
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Model": {
                "Name": "my_model",
                "Comment": "这是一个模型"
            }
        }
    }
}
```

