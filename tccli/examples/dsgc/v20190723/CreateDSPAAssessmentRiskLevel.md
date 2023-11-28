**Example 1: 示例**

xx

Input: 

```
tccli dsgc CreateDSPAAssessmentRiskLevel --cli-unfold-argument  \
    --DspaId abc \
    --RiskLevelName abc \
    --RiskLevelDescription abc \
    --IdentifyComplianceId 0 \
    --RiskLevelRule.0.Id 0 \
    --RiskLevelRule.0.SensitiveLevelId 0 \
    --RiskLevelRule.0.SensitiveLevelName abc \
    --RiskLevelRule.0.VulnerabilityLevel abc \
    --RiskLevelRule.0.RiskLevel abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

