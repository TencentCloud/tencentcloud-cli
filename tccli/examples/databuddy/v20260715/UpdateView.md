**Example 1: 修改视图信息**

修改视图的注释

Input: 

```
tccli databuddy UpdateView --cli-unfold-argument  \
    --CatalogName c4 \
    --SchemaName ss \
    --ViewName c3 \
    --NewComment capi auto test view \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "View": {
                "Name": "c3",
                "Comment": "capi auto test view"
            }
        },
        "RequestId": "f77a3fc4-7bff-4a3b-8e58-d4d7ccc0bc25"
    }
}
```

