**Example 1: DescribeTableOptimizationStrategy**

查询表级数据优化

Input: 

```
tccli tccatalog DescribeTableOptimizationStrategy --cli-unfold-argument  \
    --CatalogName justtestdlc \
    --SchemaName dlc \
    --TableName products
```

Output: 
```
{
    "Response": {
        "RequestId": "e634125c-b612-471a-90a2-d85a4e368ab2",
        "Config": {
            "SelfOptimizingEnabled": true,
            "TableExpireEnabled": false,
            "CleanOrphanFileEnabled": true,
            "CleanDanglingDeleteEnabled": false,
            "SelfOptimizingTargetSize": 10,
            "SnapshotKeepDuration": 10
        }
    }
}
```

