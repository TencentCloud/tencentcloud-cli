**Example 1: 修改函数信息**

修改函数的注释

Input: 

```
tccli databuddy UpdateFunction --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --FunctionName my_function \
    --NewComment updated function comment \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Function": {
                "Name": "my_function",
                "Comment": "updated function comment",
                "Tags": []
            }
        },
        "RequestId": "b612b753-ec7e-4fda-9eec-76f85ebd06b7"
    }
}
```

