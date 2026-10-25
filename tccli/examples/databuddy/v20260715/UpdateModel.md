**Example 1: 修改模型信息**

修改模型的名称或注释

Input: 

```
tccli databuddy UpdateModel --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ModelName my_model \
    --NewComment updated model comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Model": {
                "Name": "my_model",
                "Comment": "updated model comment",
                "LatestVersion": "1"
            }
        },
        "RequestId": "e477710a-7700-4b1d-9d5a-1f33e520f4ef"
    }
}
```

