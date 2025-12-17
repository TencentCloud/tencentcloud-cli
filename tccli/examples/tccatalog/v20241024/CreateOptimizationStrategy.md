**Example 1: CreateOptimizationStrategy**

创建数据优化策略

Input: 

```
tccli tccatalog CreateOptimizationStrategy --cli-unfold-argument  \
    --CatalogName yyyy \
    --SelfOptimizingEnabled True \
    --SelfOptimizingTargetSize 64 \
    --TableExpireEnabled True \
    --SnapshotKeepDuration 1024 \
    --CleanOrphanFileEnabled True \
    --CleanDanglingDeleteEnabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "e634125c-b612-471a-90a2-d85a4e368ab2"
    }
}
```

