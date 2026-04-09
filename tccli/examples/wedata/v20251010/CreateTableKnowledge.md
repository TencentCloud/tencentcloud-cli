**Example 1: 创建表**



Input: 

```
tccli wedata CreateTableKnowledge --cli-unfold-argument  \
    --WorkspaceId 1 \
    --Catalog asdasda \
    --Schema asda \
    --Table asdsa \
    --Description asdasd \
    --Columns.0.Name 11 \
    --Columns.0.Type string \
    --Columns.0.Description string \
    --Columns.0.Nullable True \
    --Columns.0.Comment string \
    --Metadata {"a": 1}
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorCode": 0,
            "ErrorMessage": ""
        },
        "RequestId": "fee7a2d1-5221-4275-87db-7348eb6622eb"
    }
}
```

