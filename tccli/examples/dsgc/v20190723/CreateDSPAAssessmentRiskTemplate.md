**Example 1: 创建风险评估模板**

风险评估模板---创建风险评估模板

Input: 

```
tccli dsgc CreateDSPAAssessmentRiskTemplate --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --TemplateName 风险评估模版 \
    --TemplateDescription 默认风险评估模版 \
    --RiskLevelId 10070 \
    --RiskIdList 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

