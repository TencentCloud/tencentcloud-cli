**Example 1: 查询风险等级的详情数据**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskLevelDetail --cli-unfold-argument  \
    --DspaId dspa-89cas3sq \
    --RiskLevelId 1
```

Output: 
```
{
    "Response": {
        "RiskLevelMatrix": [
            {
                "RiskLevel": "high",
                "Id": 12211,
                "SensitiveLevelId": 1,
                "SensitiveLevelName": "高",
                "VulnerabilityLevel": "high"
            },
            {
                "RiskLevel": "high",
                "Id": 12212,
                "SensitiveLevelId": 1,
                "SensitiveLevelName": "高",
                "VulnerabilityLevel": "medium"
            },
            {
                "RiskLevel": "medium",
                "Id": 12213,
                "SensitiveLevelId": 1,
                "SensitiveLevelName": "高",
                "VulnerabilityLevel": "low"
            },
            {
                "RiskLevel": "high",
                "Id": 12214,
                "SensitiveLevelId": 2,
                "SensitiveLevelName": "中",
                "VulnerabilityLevel": "high"
            },
            {
                "RiskLevel": "medium",
                "Id": 12215,
                "SensitiveLevelId": 2,
                "SensitiveLevelName": "中",
                "VulnerabilityLevel": "medium"
            },
            {
                "RiskLevel": "low",
                "Id": 12216,
                "SensitiveLevelId": 2,
                "SensitiveLevelName": "中",
                "VulnerabilityLevel": "low"
            },
            {
                "RiskLevel": "medium",
                "Id": 12217,
                "SensitiveLevelId": 3,
                "SensitiveLevelName": "低",
                "VulnerabilityLevel": "high"
            },
            {
                "RiskLevel": "low",
                "Id": 12218,
                "SensitiveLevelId": 3,
                "SensitiveLevelName": "低",
                "VulnerabilityLevel": "medium"
            },
            {
                "RiskLevel": "low",
                "Id": 12219,
                "SensitiveLevelId": 3,
                "SensitiveLevelName": "低",
                "VulnerabilityLevel": "low"
            },
            {
                "RiskLevel": "low",
                "Id": 12220,
                "SensitiveLevelId": 0,
                "SensitiveLevelName": "NotSensitive",
                "VulnerabilityLevel": "high"
            },
            {
                "RiskLevel": "low",
                "Id": 12221,
                "SensitiveLevelId": 0,
                "SensitiveLevelName": "NotSensitive",
                "VulnerabilityLevel": "medium"
            },
            {
                "RiskLevel": "low",
                "Id": 12222,
                "SensitiveLevelId": 0,
                "SensitiveLevelName": "NotSensitive",
                "VulnerabilityLevel": "low"
            }
        ],
        "RiskLevelName": "默认风险级别",
        "RiskLevelDescription": "自动化测试，勿删",
        "IdentifyComplianceId": 1,
        "IdentifyComplianceName": "通用规则集",
        "RequestId": "c92ee4ca-dad0-4e5f-ab7e-ffe693c9951c"
    }
}
```

