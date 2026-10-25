**Example 1: 修改Schema信息**

修改Schema的注释

Input: 

```
tccli databuddy UpdateSchema --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --NewComment updated schema comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Schema": {
                "Name": "my_schema",
                "Comment": "updated schema comment"
            }
        },
        "RequestId": "4a28103f-b91d-4cc9-b359-7fa6ec0e058d"
    }
}
```

