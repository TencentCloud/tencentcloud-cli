**Example 1: 查询建议的默认风险等级矩阵**



Input: 

```
tccli dsgc DecribeSuggestRiskLevelMatrix --cli-unfold-argument  \
    --DspaId dspa-1klcj34a \
    --SensitiveLevelList.0.Id 8 \
    --SensitiveLevelList.0.Name 敏感 \
    --SensitiveLevelList.0.Score 10 \
    --SensitiveLevelList.1.Id 9 \
    --SensitiveLevelList.1.Name 重要 \
    --SensitiveLevelList.1.Score 5 \
    --SensitiveLevelList.2.Id 10 \
    --SensitiveLevelList.2.Name 一般 \
    --SensitiveLevelList.2.Score 1 \
    --SensitiveLevelList.3.Id 0 \
    --SensitiveLevelList.3.Name NotSensitive \
    --SensitiveLevelList.3.Score 0 \
    --VulnerabilityLevelList.0.Name high \
    --VulnerabilityLevelList.0.Score 10 \
    --VulnerabilityLevelList.0.Id 1 \
    --VulnerabilityLevelList.1.Name medium \
    --VulnerabilityLevelList.1.Score 5 \
    --VulnerabilityLevelList.1.Id 2 \
    --VulnerabilityLevelList.2.Name low \
    --VulnerabilityLevelList.2.Score 1 \
    --VulnerabilityLevelList.2.Id 3
```

Output: 
```
{
    "Response": {
        "SuggestRiskLevelMatrix": [
            {
                "RiskLevelMatrix": [
                    {
                        "RiskScore": 100,
                        "SensitiveLevel": {
                            "Name": "敏感",
                            "Id": 8,
                            "Score": 10
                        },
                        "VulnerabilityLevel": {
                            "Name": "high",
                            "Id": 1,
                            "Score": 10
                        },
                        "RiskName": "high"
                    },
                    {
                        "RiskScore": 50,
                        "SensitiveLevel": {
                            "Name": "敏感",
                            "Id": 8,
                            "Score": 10
                        },
                        "VulnerabilityLevel": {
                            "Name": "medium",
                            "Id": 2,
                            "Score": 5
                        },
                        "RiskName": "high"
                    },
                    {
                        "RiskScore": 10,
                        "SensitiveLevel": {
                            "Name": "敏感",
                            "Id": 8,
                            "Score": 10
                        },
                        "VulnerabilityLevel": {
                            "Name": "low",
                            "Id": 3,
                            "Score": 1
                        },
                        "RiskName": "medium"
                    }
                ]
            },
            {
                "RiskLevelMatrix": [
                    {
                        "RiskScore": 50,
                        "SensitiveLevel": {
                            "Name": "重要",
                            "Id": 9,
                            "Score": 5
                        },
                        "VulnerabilityLevel": {
                            "Name": "high",
                            "Id": 1,
                            "Score": 10
                        },
                        "RiskName": "high"
                    },
                    {
                        "RiskScore": 25,
                        "SensitiveLevel": {
                            "Name": "重要",
                            "Id": 9,
                            "Score": 5
                        },
                        "VulnerabilityLevel": {
                            "Name": "medium",
                            "Id": 2,
                            "Score": 5
                        },
                        "RiskName": "medium"
                    },
                    {
                        "RiskScore": 5,
                        "SensitiveLevel": {
                            "Name": "重要",
                            "Id": 9,
                            "Score": 5
                        },
                        "VulnerabilityLevel": {
                            "Name": "low",
                            "Id": 3,
                            "Score": 1
                        },
                        "RiskName": "low"
                    }
                ]
            },
            {
                "RiskLevelMatrix": [
                    {
                        "RiskScore": 10,
                        "SensitiveLevel": {
                            "Name": "一般",
                            "Id": 10,
                            "Score": 1
                        },
                        "VulnerabilityLevel": {
                            "Name": "high",
                            "Id": 1,
                            "Score": 10
                        },
                        "RiskName": "medium"
                    },
                    {
                        "RiskScore": 5,
                        "SensitiveLevel": {
                            "Name": "一般",
                            "Id": 10,
                            "Score": 1
                        },
                        "VulnerabilityLevel": {
                            "Name": "medium",
                            "Id": 2,
                            "Score": 5
                        },
                        "RiskName": "low"
                    },
                    {
                        "RiskScore": 1,
                        "SensitiveLevel": {
                            "Name": "一般",
                            "Id": 10,
                            "Score": 1
                        },
                        "VulnerabilityLevel": {
                            "Name": "low",
                            "Id": 3,
                            "Score": 1
                        },
                        "RiskName": "low"
                    }
                ]
            },
            {
                "RiskLevelMatrix": [
                    {
                        "RiskScore": 0,
                        "SensitiveLevel": {
                            "Name": "NotSensitive",
                            "Id": 0,
                            "Score": 0
                        },
                        "VulnerabilityLevel": {
                            "Name": "high",
                            "Id": 1,
                            "Score": 10
                        },
                        "RiskName": "low"
                    },
                    {
                        "RiskScore": 0,
                        "SensitiveLevel": {
                            "Name": "NotSensitive",
                            "Id": 0,
                            "Score": 0
                        },
                        "VulnerabilityLevel": {
                            "Name": "medium",
                            "Id": 2,
                            "Score": 5
                        },
                        "RiskName": "low"
                    },
                    {
                        "RiskScore": 0,
                        "SensitiveLevel": {
                            "Name": "NotSensitive",
                            "Id": 0,
                            "Score": 0
                        },
                        "VulnerabilityLevel": {
                            "Name": "low",
                            "Id": 3,
                            "Score": 1
                        },
                        "RiskName": "low"
                    }
                ]
            }
        ],
        "RequestId": "e740e934-03d9-4ed8-a70e-1aeb4f1c131d"
    }
}
```

