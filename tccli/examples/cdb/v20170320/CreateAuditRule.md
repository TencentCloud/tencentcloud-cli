**Example 1: 创建审计规则 ( 全审计 )**



Input: 

```
tccli cdb CreateAuditRule --cli-unfold-argument  \
    --Description audit_test \
    --AuditAll true \
    --RuleName audit1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "RuleId": "cdbrule-qwerasdf"
    }
}
```

**Example 2: 创建审计规则 ( 规则审计 )**



Input: 

```
tccli cdb CreateAuditRule --cli-unfold-argument  \
    --RuleFilters.0.Compare INC \
    --RuleFilters.0.Type DB \
    --RuleFilters.0.Value CDB \
    --Description audit_test \
    --RuleName audit1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "RuleId": "cdbrule-qwerasdf"
    }
}
```

