**Example 1: 创建Schema**



Input: 

```
tccli databuddy CreateSchema --cli-unfold-argument  \
    --CatalogName my_catalog \
    --Name my_schema \
    --WorkspaceId 17697667906247629 \
    --Comment 这是一个Schema
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Schema": {
                "Name": "my_schema",
                "Comment": "这是一个Schema"
            }
        }
    }
}
```

