**Example 1: 修改安全配置**

修改a.eotest.com域名七层安全配置

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

**Example 2: 修改安全配置中的例外规则并加白字段的场景**

在WAF防护中，如果业务存在某个场景（如路径为/skipwaf的HTTP请求）需要对部分字段（如HTTP Header的全部Key）进行加白以此来跳过WAF安全防护，则可以使用如下配置。

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --Entity *.eotest.com \
    --SecurityConfig.ExceptConfig.Switch on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.Action skip \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchContent /skipwaf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchFrom cgi \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchParam  \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.Operator equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.Type partial \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Module waf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Include 106247778 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchContentType  \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchFromType  \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Selector keys \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Type header_fields \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleID 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleName first_webshell \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RulePriority 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleStatus on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.UpdateTime 2022-09-22T03:00:10Z \
    --ZoneId zone-fa89j239a
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae44"
    }
}
```

**Example 3: 修改安全配置中的例外规则并加白Header指定key字段的场景**

在WAF防护中，如果业务存在某个场景（如路径为/skipwaf的HTTP请求）需要对部分字段（如HTTP Header中的YourSkipHeader对应的Value）进行加白以此来跳过WAF安全防护，则可以使用如下配置。

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --Entity *.eotest.com \
    --SecurityConfig.ExceptConfig.Switch on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.Action skip \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchContent /skipwaf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchFrom cgi \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchParam  \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.Operator equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.Type partial \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Module waf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Include 106247778 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchContentType  \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchFrom YourSkipHeader \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchFromType equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Selector values \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Type header_fields \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleID 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleName first_webshell \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RulePriority 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleStatus on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.UpdateTime 2022-09-22T03:00:10Z \
    --ZoneId zone-fa89j239a
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae66"
    }
}
```

