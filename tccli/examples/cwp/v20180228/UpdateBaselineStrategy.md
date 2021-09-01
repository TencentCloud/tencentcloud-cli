**Example 1: 更新基线策略信息**

根据基线策略id更新策略信息

Input: 

```
tccli cwp UpdateBaselineStrategy --cli-unfold-argument  \
    --StrategyName "test" \
    --ScanCycle 1 \
    --ScanAt "00:00:00" \
    --CategoryIds 1 \
    --IsGlobal 1 \
    --MachineType "CVM" \
    --RegionCode "ab-bj" \
    --Quuids "123" \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234"
    }
}
```

