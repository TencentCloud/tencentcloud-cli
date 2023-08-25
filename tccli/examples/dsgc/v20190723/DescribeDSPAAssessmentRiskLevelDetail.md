**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskLevelDetail --cli-unfold-argument  \
    --DspaId abc \
    --RiskLevelId 0
```

Output: 
```
{
    "Response": {
        "RiskLevelName": "abc",
        "RiskLevelDescription": "abc",
        "IdentifyComplianceId": 0,
        "IdentifyComplianceName": "abc",
        "RiskLevelMatrix": [
            {
                "Id": 0,
                "SensitiveLevelId": 0,
                "SensitiveLevelName": "abc",
                "VulnerabilityLevel": "abc",
                "RiskLevel": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

