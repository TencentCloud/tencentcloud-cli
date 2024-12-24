**Example 1: 创建风险等级**

风险项页面---创建风险等级

Input: 

```
tccli dsgc CreateDSPAAssessmentRiskLevel --cli-unfold-argument  \
    --DspaId dspa-a1b2c3d4 \
    --RiskLevelName 默认评估分级模板 \
    --RiskLevelDescription 默认评估分级模板 \
    --IdentifyComplianceId 3 \
    --RiskLevelRule.0.SensitiveLevelId 1 \
    --RiskLevelRule.0.SensitiveLevelName 高 \
    --RiskLevelRule.0.VulnerabilityLevel high \
    --RiskLevelRule.0.RiskLevel high \
    --RiskLevelRule.1.SensitiveLevelId 1 \
    --RiskLevelRule.1.SensitiveLevelName 高 \
    --RiskLevelRule.1.VulnerabilityLevel medium \
    --RiskLevelRule.1.RiskLevel high \
    --RiskLevelRule.2.SensitiveLevelId 1 \
    --RiskLevelRule.2.SensitiveLevelName 高 \
    --RiskLevelRule.2.VulnerabilityLevel low \
    --RiskLevelRule.2.RiskLevel medium \
    --RiskLevelRule.3.SensitiveLevelId 2 \
    --RiskLevelRule.3.SensitiveLevelName 中 \
    --RiskLevelRule.3.VulnerabilityLevel high \
    --RiskLevelRule.3.RiskLevel high \
    --RiskLevelRule.4.SensitiveLevelId 2 \
    --RiskLevelRule.4.SensitiveLevelName 中 \
    --RiskLevelRule.4.VulnerabilityLevel medium \
    --RiskLevelRule.4.RiskLevel medium \
    --RiskLevelRule.5.SensitiveLevelId 2 \
    --RiskLevelRule.5.SensitiveLevelName 中 \
    --RiskLevelRule.5.VulnerabilityLevel low \
    --RiskLevelRule.5.RiskLevel low \
    --RiskLevelRule.6.SensitiveLevelId 3 \
    --RiskLevelRule.6.SensitiveLevelName 低 \
    --RiskLevelRule.6.VulnerabilityLevel high \
    --RiskLevelRule.6.RiskLevel medium \
    --RiskLevelRule.7.SensitiveLevelId 3 \
    --RiskLevelRule.7.SensitiveLevelName 低 \
    --RiskLevelRule.7.VulnerabilityLevel medium \
    --RiskLevelRule.7.RiskLevel low \
    --RiskLevelRule.8.SensitiveLevelId 3 \
    --RiskLevelRule.8.SensitiveLevelName 低 \
    --RiskLevelRule.8.VulnerabilityLevel low \
    --RiskLevelRule.8.RiskLevel low \
    --RiskLevelRule.9.SensitiveLevelId 0 \
    --RiskLevelRule.9.SensitiveLevelName NotSensitive \
    --RiskLevelRule.9.VulnerabilityLevel high \
    --RiskLevelRule.9.RiskLevel low \
    --RiskLevelRule.10.SensitiveLevelId 0 \
    --RiskLevelRule.10.SensitiveLevelName NotSensitive \
    --RiskLevelRule.10.VulnerabilityLevel medium \
    --RiskLevelRule.10.RiskLevel low \
    --RiskLevelRule.11.SensitiveLevelId 0 \
    --RiskLevelRule.11.SensitiveLevelName NotSensitive \
    --RiskLevelRule.11.VulnerabilityLevel low \
    --RiskLevelRule.11.RiskLevel low
```

Output: 
```
{
    "Response": {
        "RequestId": "e298a8a2-e620-4cc5-9b85-4f0e22d273bf"
    }
}
```

