**Example 1: 示例**

风险项页面----修改风险等级的详情数据

Input: 

```
tccli dsgc ModifyDSPAAssessmentRiskLevel --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --ModifyRiskItem.0.Id 1278 \
    --ModifyRiskItem.0.SensitiveLevelId 12098 \
    --ModifyRiskItem.0.SensitiveLevelName 高危 \
    --ModifyRiskItem.0.VulnerabilityLevel high \
    --ModifyRiskItem.0.RiskLevel high \
    --RiskLevelName 高风险 \
    --RiskLevelDescription 高风险 \
    --RiskId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

