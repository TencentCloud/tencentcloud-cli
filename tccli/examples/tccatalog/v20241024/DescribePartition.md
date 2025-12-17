**Example 1: DescribePartition示例**



Input: 

```
tccli tccatalog DescribePartition --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --TableName t1 \
    --PartitionName p1
```

Output: 
```
{
    "Response": {
        "Partition": null,
        "RequestId": "b9488675-cc4e-472f-94ce-3ec2efb32dae"
    }
}
```

