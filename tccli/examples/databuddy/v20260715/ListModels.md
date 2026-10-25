**Example 1: 分页获取模型列表**



Input: 

```
tccli databuddy ListModels --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --MaxResults 10 \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Items": [
                {
                    "Name": "my_model",
                    "Comment": "这是一个模型"
                }
            ],
            "TotalCount": "1",
            "NextPageToken": ""
        }
    }
}
```

