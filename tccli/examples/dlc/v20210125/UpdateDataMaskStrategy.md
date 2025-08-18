**Example 1: 更新数据脱敏策略**



Input: 

```
tccli dlc UpdateDataMaskStrategy --cli-unfold-argument  \
    --Strategy.StrategyId c82f17bd-f577-4930-a8ef-83b9647259b8 \
    --Strategy.StrategyName default_strategy \
    --Strategy.StrategyType  \
    --Strategy.StrategyDesc  \
    --Strategy.Groups.0.WorkGroupId 225249 \
    --Strategy.Groups.0.StrategyType MASK_SHOW_LAST_4 \
    --Strategy.Groups.1.WorkGroupId 225237 \
    --Strategy.Groups.1.StrategyType MASK_HASH
```

Output: 
```
{
    "Response": {
        "RequestId": "0d2dc2eb-0a9c-483b-9454-e7e8db604507"
    }
}
```

