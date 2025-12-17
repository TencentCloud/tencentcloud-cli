**Example 1: 移除分区**



Input: 

```
tccli tccatalog RemovePartitionField --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --TableName t1 \
    --Partitioning.Strategy YearPartitioning \
    --Partitioning.YearPartitioning.FieldName p1
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
        "RequestId": "550a33ba-37bf-416c-a583-aa01bf2bfcd4"
    }
}
```

