**Example 1: 修改分类分级模板**

xx

Input: 

```
tccli dsgc ModifyDSPAComplianceGroup --cli-unfold-argument  \
    --Name task \
    --DspaId dspa-001 \
    --LevelGroupId 1 \
    --ComplianceGroupRules.0.RuleId 2 \
    --ComplianceGroupRules.0.CategoryId 3 \
    --ComplianceGroupRules.0.LevelId 2 \
    --ComplianceGroupId 1 \
    --Description 1
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

