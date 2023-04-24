**Example 1: 开通实例审计服务**

无

Input: 

```
tccli cdb OpenAuditService --cli-unfold-argument  \
    --InstanceId cdb-3u8h3h1w \
    --LogExpireDay 30 \
    --HighLogExpireDay 7 \
    --AuditRuleFilters.0.RuleFilters.0.Compare NEQ \
    --AuditRuleFilters.0.RuleFilters.0.Type host \
    --AuditRuleFilters.0.RuleFilters.0.Value 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "43-12121-812w1221213-62usf6123"
    }
}
```

