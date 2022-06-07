**Example 1: 修改安全配置**



Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --Entity xx \
    --Config.WafConfig.Switch xx \
    --Config.WafConfig.WafRules.Switch xx \
    --Config.WafConfig.WafRules.BlockRuleIDs 0 \
    --Config.WafConfig.Mode xx \
    --Config.WafConfig.Level xx \
    --Config.DdosConfig.Switch xx \
    --Config.RateLimitConfig.Switch xx \
    --Config.RateLimitConfig.UserRules.0.UpdateTime 2020-09-22T00:00:00+00:00 \
    --Config.RateLimitConfig.UserRules.0.RuleID 0 \
    --Config.RateLimitConfig.UserRules.0.PunishTimeUnit xx \
    --Config.RateLimitConfig.UserRules.0.RulePriority 0 \
    --Config.RateLimitConfig.UserRules.0.FreqFields xx \
    --Config.RateLimitConfig.UserRules.0.Period 0 \
    --Config.RateLimitConfig.UserRules.0.PunishTime 0 \
    --Config.RateLimitConfig.UserRules.0.Action xx \
    --Config.RateLimitConfig.UserRules.0.RuleName xx \
    --Config.RateLimitConfig.UserRules.0.Threshold 0 \
    --Config.RateLimitConfig.UserRules.0.RuleStatus xx \
    --Config.RateLimitConfig.UserRules.0.Conditions.0.MatchParam xx \
    --Config.RateLimitConfig.UserRules.0.Conditions.0.Operator xx \
    --Config.RateLimitConfig.UserRules.0.Conditions.0.MatchFrom xx \
    --Config.RateLimitConfig.UserRules.0.Conditions.0.MatchContent xx \
    --Config.AclConfig.Switch xx \
    --Config.AclConfig.UserRules.0.UpdateTime 2020-09-22T00:00:00+00:00 \
    --Config.AclConfig.UserRules.0.RuleID 0 \
    --Config.AclConfig.UserRules.0.RulePriority 0 \
    --Config.AclConfig.UserRules.0.RuleName xx \
    --Config.AclConfig.UserRules.0.Action xx \
    --Config.AclConfig.UserRules.0.RuleStatus xx \
    --Config.AclConfig.UserRules.0.Conditions.0.MatchParam xx \
    --Config.AclConfig.UserRules.0.Conditions.0.Operator xx \
    --Config.AclConfig.UserRules.0.Conditions.0.MatchFrom xx \
    --Config.AclConfig.UserRules.0.Conditions.0.MatchContent xx \
    --ZoneId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae23"
    }
}
```

