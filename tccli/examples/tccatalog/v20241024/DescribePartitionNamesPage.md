**Example 1: DescribePartitionNamesPage示例**



Input: 

```
tccli tccatalog DescribePartitionNamesPage --cli-unfold-argument  \
    --CatalogName layyu_c1 \
    --SchemaName s1 \
    --TableName t1
```

Output: 
```
{
    "Response": {
        "PartitionNames": [],
        "SnapshotId": "",
        "TotalCount": 0,
        "RequestId": "ce428c12-9f62-47a1-92ad-f383c76131e7"
    }
}
```

