**Example 1: 修改表信息**

修改表的名称或注释

Input: 

```
tccli databuddy UpdateTable --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --TableName my_table \
    --NewComment updated table comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Table": {
                "Name": "my_table",
                "Comment": "updated table comment"
            }
        },
        "RequestId": "c7553f90-800d-47d0-be3f-f84ed3686718"
    }
}
```

