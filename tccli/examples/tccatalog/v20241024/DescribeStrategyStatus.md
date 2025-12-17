**Example 1: DescribeStrategyStatus**

查询数据优化策略状态

Input: 

```
tccli tccatalog DescribeStrategyStatus --cli-unfold-argument  \
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

