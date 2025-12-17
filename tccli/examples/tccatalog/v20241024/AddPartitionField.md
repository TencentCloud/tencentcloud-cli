**Example 1: AddPartitionField示例**



Input: 

```
tccli tccatalog AddPartitionField --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --TableName t1 \
    --Partitioning.Strategy YearPartitioning \
    --Partitioning.YearPartitioning.FieldName f1
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
        "RequestId": "8e19cd27-37bd-4541-a1fb-2c9134a73b2c"
    }
}
```

