**Example 1: 获取模型详情**



Input: 

```
tccli databuddy GetModel --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ModelName my_model \
    --WorkspaceId 17697667906247629
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

