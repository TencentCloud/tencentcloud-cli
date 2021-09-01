**Example 1: 创建基线策略**

根据基线信息创建基线策略

Input: 

```
tccli yunjing CreateBaselineStrategy --cli-unfold-argument  \
    --StrategyName "test" \
    --ScanCycle 1 \
    --ScanAt "00:00:00" \
    --CategoryIds [1,2,3] \
    --IsGlobal 1 \
    --MachineType "CVM" \
    --RegionCode "ab-bj" \
    --Quuids ['quuid1','quuid2']
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234"
    }
}
```

