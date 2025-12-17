**Example 1: ModifySchemaComment示例**



Input: 

```
tccli tccatalog ModifySchemaComment --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName dwd \
    --NewComment 业务数据明细
```

Output: 
```
{
    "Response": {
        "Schema": {
            "Name": "dwd",
            "Comment": "业务数据明细层"
        },
        "RequestId": "fafesfsfsafeafa"
    }
}
```

