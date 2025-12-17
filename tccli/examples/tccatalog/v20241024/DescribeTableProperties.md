**Example 1: DescribeTableProperties**

查询表级属性

Input: 

```
tccli tccatalog DescribeTableProperties --cli-unfold-argument  \
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

