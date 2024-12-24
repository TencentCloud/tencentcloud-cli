**Example 1: 新增分类分级模板**



Input: 

```
tccli dsgc CreateDSPAComplianceGroup --cli-unfold-argument  \
    --LevelGroupId 1 \
    --DspaId dspa-001 \
    --ComplianceGroupRules.0.RuleId 2 \
    --ComplianceGroupRules.0.CategoryId 3 \
    --ComplianceGroupRules.0.LevelId 2 \
    --Name task \
    --Description 分类分级模版描述
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "ComplianceGroupId": 1
    }
}
```

