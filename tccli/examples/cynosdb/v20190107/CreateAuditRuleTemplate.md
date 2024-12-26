**Example 1: 创建审计规则模板**

创建审计规则模板

Input: 

```
tccli cynosdb CreateAuditRuleTemplate --cli-unfold-argument  \
    --RuleFilters.0.Type host \
    --RuleFilters.0.Compare EQS \
    --RuleFilters.0.Value 100.122.76.176 10.0.0.9 \
    --RuleFilters.1.Type user \
    --RuleFilters.1.Compare EQS \
    --RuleFilters.1.Value wy andy \
    --RuleFilters.2.Type sqlType \
    --RuleFilters.2.Compare EQS \
    --RuleFilters.2.Value Update Delete \
    --RuleTemplateName andy \
    --Description andy模板
```

Output: 
```
{
    "Response": {
        "RuleTemplateId": "cynosdb-rt-ws23fwu8",
        "RequestId": "43-12121-812w1221213-62usf9093"
    }
}
```

