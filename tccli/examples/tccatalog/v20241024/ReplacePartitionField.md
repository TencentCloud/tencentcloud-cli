**Example 1: ReplacePartitionField**



Input: 

```
tccli tccatalog ReplacePartitionField --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --TableName t1 \
    --OldPartitioning.Strategy YearPartitioning \
    --OldPartitioning.YearPartitioning.FieldName FieldName1 \
    --NewPartitioning.Strategy MonthPartitioning \
    --NewPartitioning.MonthPartitioning.FieldName FieldName1
```

Output: 
```
{
    "Response": {
        "Table": {
            "Comment": "",
            "Name": "",
            "TableFormat": ""
        },
        "RequestId": "2afb9186-33a4-480e-be9e-c15808774744"
    }
}
```

