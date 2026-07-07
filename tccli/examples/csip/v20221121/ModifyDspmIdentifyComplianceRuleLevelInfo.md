**Example 1: 修改dspm数据识别模板数据项关联级别信息**



Input: 

```
tccli csip ModifyDspmIdentifyComplianceRuleLevelInfo --cli-unfold-argument  \
    --ComplianceId 10482 \
    --RuleId 5917 \
    --LevelId 2 \
    --MemberId mem-1231es1s
```

Output: 
```
{
    "Response": {
        "RequestId": "8f69b71e-000f-4c1e-9b06-488d6fb453cb"
    }
}
```

