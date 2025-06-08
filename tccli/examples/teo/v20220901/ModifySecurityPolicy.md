**Example 1: 修改域名策略**

修改eotest.com站点下a.eotest.com域名策略

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity Host \
    --Host a.eotest.com \
    --SecurityPolicy.ExceptionRules.Rules.0.Id 1492837231 \
    --SecurityPolicy.ExceptionRules.Rules.0.Name ExampleSkipModule \
    --SecurityPolicy.ExceptionRules.Rules.0.Condition ${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST'] \
    --SecurityPolicy.ExceptionRules.Rules.0.SkipScope WebSecurityModules \
    --SecurityPolicy.ExceptionRules.Rules.0.WebSecurityModulesForException websec-mod-custom-rules websec-mod-rate-limiting \
    --SecurityPolicy.ExceptionRules.Rules.0.Enabled On \
    --SecurityPolicy.ExceptionRules.Rules.1.Id 1492837231 \
    --SecurityPolicy.ExceptionRules.Rules.1.Name SampleSkipManagedRule \
    --SecurityPolicy.ExceptionRules.Rules.1.Condition ${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST'] \
    --SecurityPolicy.ExceptionRules.Rules.1.SkipScope ManagedRules \
    --SecurityPolicy.ExceptionRules.Rules.1.SkipOption SkipOnAllRequestFields \
    --SecurityPolicy.ExceptionRules.Rules.1.ManagedRulesForException 4401215074 4368124487 \
    --SecurityPolicy.ExceptionRules.Rules.1.Enabled On \
    --SecurityPolicy.ExceptionRules.Rules.2.Id 1492837231 \
    --SecurityPolicy.ExceptionRules.Rules.2.Name SampleSkipManagedRule \
    --SecurityPolicy.ExceptionRules.Rules.2.Condition ${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST'] \
    --SecurityPolicy.ExceptionRules.Rules.2.SkipScope ManagedRules \
    --SecurityPolicy.ExceptionRules.Rules.2.SkipOption SkipOnAllRequestFields \
    --SecurityPolicy.ExceptionRules.Rules.2.ManagedRuleGroupsForException wafgroup-sql-injection-attacks \
    --SecurityPolicy.ExceptionRules.Rules.2.Enabled On \
    --SecurityPolicy.ExceptionRules.Rules.3.Id 1492837231 \
    --SecurityPolicy.ExceptionRules.Rules.3.Name SampleSkipManagedRuleForField \
    --SecurityPolicy.ExceptionRules.Rules.3.Condition ${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] and ${http.request.method} in ['POST'] \
    --SecurityPolicy.ExceptionRules.Rules.3.SkipScope ManagedRules \
    --SecurityPolicy.ExceptionRules.Rules.3.ManagedRulesForException 4401215074 4368124487 \
    --SecurityPolicy.ExceptionRules.Rules.3.SkipOption SkipOnSpecifiedRequestFields \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.0.Scope cookie \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.0.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.0.TargetField key \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.1.Scope cookie \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.1.Condition ${key} in ['session-id'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.1.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.2.Scope cookie \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.2.Condition ${key} in ['account-id'] and ${value} like ['prefix-*'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.2.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.3.Scope header \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.3.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.3.TargetField key \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.4.Scope header \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.4.Condition ${key} in ['x-trace-id'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.4.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.5.Scope header \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.5.Condition ${key} like ['x-auth-*'] and ${value} like ['Bearer *'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.5.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.6.Scope uri.query \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.6.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.6.TargetField key \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.7.Scope uri.query \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.7.Condition ${key} in ['action'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.7.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.8.Scope uri.query \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.8.Condition ${key} in ['action'] and ${value} in ['upload', 'delete'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.8.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.9.Scope uri \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.9.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.9.TargetField query \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.10.Scope uri \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.10.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.10.TargetField path \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.11.Scope uri \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.11.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.11.TargetField fullpath \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.12.Scope body.json \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.12.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.12.TargetField key \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.13.Scope body.json \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.13.Condition ${key} in ['user.id'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.13.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.14.Scope body.json \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.14.Condition ${key} in ['user.id'] and ${value} in ['1234', '5678'] \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.14.TargetField value \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.15.Scope body \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.15.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.15.TargetField fullbody \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.16.Scope body \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.16.Condition  \
    --SecurityPolicy.ExceptionRules.Rules.3.RequestFieldsForException.16.TargetField multipart \
    --SecurityPolicy.ExceptionRules.Rules.3.Enabled On \
    --SecurityPolicy.CustomRules.Rules.0.Id 1492837231 \
    --SecurityPolicy.CustomRules.Rules.0.Name SampleBasicACLRule \
    --SecurityPolicy.CustomRules.Rules.0.Condition ${http.request.ip} in ['1.1.1.1', '10.10.10.0/24', ${security.ip_group['123'@'zone-2xsnpvkhdjes']} ] \
    --SecurityPolicy.CustomRules.Rules.0.Action.Name Deny \
    --SecurityPolicy.CustomRules.Rules.0.Priority 10 \
    --SecurityPolicy.CustomRules.Rules.0.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.AdaptiveFrequencyControl.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.AdaptiveFrequencyControl.Sensitivity Loose \
    --SecurityPolicy.HttpDDoSProtection.AdaptiveFrequencyControl.Action.Name Monitor \
    --SecurityPolicy.HttpDDoSProtection.ClientFiltering.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.ClientFiltering.Action.Name Monitor \
    --SecurityPolicy.HttpDDoSProtection.BandwidthAbuseDefense.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.BandwidthAbuseDefense.Action.Name Monitor \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.Action.Name Monitor \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.MinimalRequestBodyTransferRate.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.MinimalRequestBodyTransferRate.MinimalAvgTransferRateThreshold 50bps \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.MinimalRequestBodyTransferRate.CountingPeriod 60s \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.RequestBodyTransferTimeout.Enabled on \
    --SecurityPolicy.HttpDDoSProtection.SlowAttackDefense.RequestBodyTransferTimeout.IdleTimeout 5s \
    --SecurityPolicy.RateLimitingRules.Rules.0.Enabled on \
    --SecurityPolicy.RateLimitingRules.Rules.0.Name SampleHttpDdosRule \
    --SecurityPolicy.RateLimitingRules.Rules.0.Condition ${http.request.uri.path} in ['/api/v3/test','/api/v3/submit'] \
    --SecurityPolicy.RateLimitingRules.Rules.0.CountBy http.request.ip http.request.cookies['UserSession'] \
    --SecurityPolicy.RateLimitingRules.Rules.0.MaxRequestThreshold 1000 \
    --SecurityPolicy.RateLimitingRules.Rules.0.CountingPeriod 2m \
    --SecurityPolicy.RateLimitingRules.Rules.0.ActionDuration 20h \
    --SecurityPolicy.RateLimitingRules.Rules.0.Action.Name ManagedChallenge \
    --SecurityPolicy.RateLimitingRules.Rules.0.Id 2181399690 \
    --SecurityPolicy.RateLimitingRules.Rules.0.Priority 100 \
    --SecurityPolicy.ManagedRules.Enabled on \
    --SecurityPolicy.ManagedRules.AutoUpdate.AutoUpdateToLatestVersion off \
    --SecurityPolicy.ManagedRules.AutoUpdate.RulesetVersion 2023-12-21T12:00:32Z \
    --SecurityPolicy.ManagedRules.SemanticAnalysis on \
    --SecurityPolicy.ManagedRules.DetectionOnly on \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.GroupId wafmanagedrulegroup-vulnerability-scanners \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.SensitivityLevel wafmanagedrule-sensitivity-level-extreme \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.Action.Name Monitor
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-777c481da684"
    }
}
```

**Example 2: 修改模板策略**

修改eotest.com站点下temp-00iel413模板策略

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity Template \
    --TemplateId temp-00iel413 \
    --SecurityPolicy.CustomRules.Rules.0.Id 1492837231 \
    --SecurityPolicy.CustomRules.Rules.0.Name SampleBasicACLRule \
    --SecurityPolicy.CustomRules.Rules.0.Condition ${http.request.ip} in ['1.1.1.1', '10.10.10.0/24', ${security.ip_group['123'@'zone-2xsnpvkhdjes']} ] \
    --SecurityPolicy.CustomRules.Rules.0.Action.Name Deny \
    --SecurityPolicy.CustomRules.Rules.0.Priority 10 \
    --SecurityPolicy.CustomRules.Rules.0.Enabled on
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-777c481da684"
    }
}
```

**Example 3: 修改站点级策略**

修改eotest.com站点级策略

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity ZoneDefaultPolicy \
    --SecurityPolicy.ManagedRules.Enabled on \
    --SecurityPolicy.ManagedRules.AutoUpdate.AutoUpdateToLatestVersion off \
    --SecurityPolicy.ManagedRules.AutoUpdate.RulesetVersion 2023-12-21T12:00:32Z \
    --SecurityPolicy.ManagedRules.SemanticAnalysis on \
    --SecurityPolicy.ManagedRules.DetectionOnly on \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.GroupId wafmanagedrulegroup-vulnerability-scanners \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.SensitivityLevel wafmanagedrule-sensitivity-level-extreme \
    --SecurityPolicy.ManagedRules.ManagedRuleGroups.0.Action.Name Monitor
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-777c481da684"
    }
}
```

**Example 4: 修改安全配置**

修改a.eotest.com域名七层安全配置

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity a.eotest.com \
    --SecurityConfig.WafConfig.Switch on \
    --SecurityConfig.WafConfig.WafRule.Switch on \
    --SecurityConfig.WafConfig.WafRule.BlockRuleIDs 162502146 \
    --SecurityConfig.WafConfig.Mode block \
    --SecurityConfig.WafConfig.Level loose
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae23"
    }
}
```

**Example 5: 修改安全配置中的例外规则并加白字段的场景**

在WAF防护中，如果业务存在某个场景（如路径为/skipwaf的HTTP请求）需要对部分字段（如HTTP Header的全部Key）进行加白以此来跳过WAF安全防护，则可以使用如下配置。

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity *.eotest.com \
    --SecurityConfig.ExceptConfig.Switch on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.Action skip \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchContent /skipwaf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchFrom cgi \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.Operator equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.Type partial \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Module waf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Include 106247778 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Selector keys \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Type header_fields \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleID 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleName first_webshell \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RulePriority 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleStatus on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.UpdateTime 2022-09-22T03:00:10Z
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae44"
    }
}
```

**Example 6: 修改安全配置中的例外规则并加白Header指定key字段的场景**

在WAF防护中，如果业务存在某个场景（如路径为/skipwaf的HTTP请求）需要对部分字段（如HTTP Header中的YourSkipHeader对应的Value）进行加白以此来跳过WAF安全防护，则可以使用如下配置。

Input: 

```
tccli teo ModifySecurityPolicy --cli-unfold-argument  \
    --ZoneId zone-fa89j239a \
    --Entity *.eotest.com \
    --SecurityConfig.ExceptConfig.Switch on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.Action skip \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchContent /skipwaf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.MatchFrom cgi \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleConditions.0.Operator equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.Type partial \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Module waf \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.PartialModules.0.Include 106247778 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchFrom YourSkipHeader \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.MatchFromType equal \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Selector values \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.ExceptUserRuleScope.SkipConditions.0.Type header_fields \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleID 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleName first_webshell \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RulePriority 0 \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.RuleStatus on \
    --SecurityConfig.ExceptConfig.ExceptUserRules.0.UpdateTime 2022-09-22T03:00:10Z
```

Output: 
```
{
    "Response": {
        "RequestId": "08b32010-ab25-42a4-b923-2e6c481dae66"
    }
}
```

