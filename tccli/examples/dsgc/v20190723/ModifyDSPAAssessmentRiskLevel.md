**Example 1: xx**

xx

Input: 

```
tccli dsgc ModifyDSPAAssessmentRiskLevel --cli-unfold-argument  \
    --DspaId abc \
    --ModifyRiskItem.0.Id 0 \
    --ModifyRiskItem.0.SensitiveLevelId 0 \
    --ModifyRiskItem.0.SensitiveLevelName abc \
    --ModifyRiskItem.0.VulnerabilityLevel abc \
    --ModifyRiskItem.0.RiskLevel abc \
    --RiskLevelName abc \
    --RiskLevelDescription abc \
    --RiskId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

