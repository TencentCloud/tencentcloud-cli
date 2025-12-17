**Example 1: DropPartition示例**



Input: 

```
tccli tccatalog DropPartition --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1 \
    --TableName t1 \
    --PartitionName dt=20201014
```

Output: 
```
{
    "Response": {
        "Dropped": true,
        "RequestId": "969eed12-b38d-48cf-8b4e-5de247ab773a"
    }
}
```

