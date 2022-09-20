**Example 1: 修改安全配置**



Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --Entity a.eotest.com \
    --SecurityConfig.WafConfig.Switch on \
    --SecurityConfig.WafConfig.WafRule.Switch on \
    --SecurityConfig.WafConfig.WafRule.BlockRuleIDs 162502146 \
    --SecurityConfig.WafConfig.Mode block \
    --SecurityConfig.WafConfig.Level loose \
    --ZoneId zone-fa89j239a
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae23"
    }
}
```

