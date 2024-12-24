**Example 1: 示例**

风险模板---修改风险模板

Input: 

```
tccli dsgc ModifyDSPAAssessmentRiskTemplate --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --TemplateName 高风险模版 \
    --TemplateDescription 高风险模版 \
    --RiskIdList 1298 \
    --TemplateId 1 \
    --RiskLevelId 1238
```

Output: 
```
{
    "Response": {
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

