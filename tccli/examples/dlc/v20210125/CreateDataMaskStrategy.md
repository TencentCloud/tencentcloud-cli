**Example 1: 创建数据脱敏策略**



Input: 

```
tccli dlc CreateDataMaskStrategy --cli-unfold-argument  \
    --Strategy.StrategyName create_data_mask_tag \
    --Strategy.Groups.0.WorkGroupId 46920 \
    --Strategy.Groups.0.StrategyType MASK_HASH
```

Output: 
```
{
    "Response": {
        "RequestId": "812228c6-45c7-43a2-af77-c7e67dc0b524"
    }
}
```

