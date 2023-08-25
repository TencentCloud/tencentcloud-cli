**Example 1: 创建合规组分类规则关联关系**

创建合规组分类规则关联关系

Input: 

```
tccli dsgc CreateDSPAComplianceRules --cli-unfold-argument  \
    --DspaId dspa-001 \
    --CategoryId 1 \
    --ComplianceId 1 \
    --Rules.0.RuleId 1 \
    --Rules.0.LevelId 5 \
    --Rules.1.RuleId 2 \
    --Rules.1.LevelId 6
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

