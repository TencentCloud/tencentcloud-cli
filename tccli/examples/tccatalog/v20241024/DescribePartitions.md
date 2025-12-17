**Example 1: DescribePartitions示例**



Input: 

```
tccli tccatalog DescribePartitions --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --TableName t1 \
    --PartitionNames p1
```

Output: 
```
{
    "Response": {
        "Partitions": null,
        "RequestId": "cb072376-d0a9-4506-a0d2-31bb12e0a304"
    }
}
```

