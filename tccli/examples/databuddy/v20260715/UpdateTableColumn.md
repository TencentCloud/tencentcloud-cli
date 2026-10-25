**Example 1: 修改表字段描述**

修改表中一个或多个字段的注释

Input: 

```
tccli databuddy UpdateTableColumn --cli-unfold-argument  \
    --CatalogName my_catalog \
    --SchemaName my_schema \
    --TableName my_table \
    --WorkspaceId 17697667906247629 \
    --Columns.0.Name col1 \
    --Columns.0.Comment updated column comment
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true,
            "FailedColumns": []
        },
        "RequestId": "dc612ad6-cce7-440c-a53f-b6335c43a0ef"
    }
}
```

