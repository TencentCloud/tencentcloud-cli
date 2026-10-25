**Example 1: 删除视图**



Input: 

```
tccli databuddy DeleteView --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --ViewName my_view \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "Data": {
            "Result": true
        }
    }
}
```

