**Example 1: 创建基线策略**

根据基线信息创建基线策略

Input: 

```
tccli cwp CreateBaselineStrategy --cli-unfold-argument  \
    --StrategyName istrategy \
    --ScanCycle 1 \
    --ScanAt 00:00:00 \
    --CategoryIds 1 \
    --IsGlobal 1 \
    --MachineType CVM \
    --RegionCode ab-bj \
    --Quuids "657f3c29-4bc9-4c48-a8d6-de5bd14ffc67"
```

Output: 
```
{
    "Response": {
        "RequestId": "657f3c29-4bc9-4c48-a8d6-de5bd14ffc67"
    }
}
```

