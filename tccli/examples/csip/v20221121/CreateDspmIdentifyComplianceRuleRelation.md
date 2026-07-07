**Example 1: 创建dspm数据识别模板数据项关联**



Input: 

```
tccli csip CreateDspmIdentifyComplianceRuleRelation --cli-unfold-argument  \
    --ComplianceId 10001 \
    --CategoryId 358 \
    --Rules.0.RuleId 5800 \
    --Rules.0.LevelId 1 \
    --MemberId mem-12e1ds1d
```

Output: 
```
{
    "Response": {
        "RequestId": "e8b7623b-7fef-4a18-85a1-57565f0fa612"
    }
}
```

