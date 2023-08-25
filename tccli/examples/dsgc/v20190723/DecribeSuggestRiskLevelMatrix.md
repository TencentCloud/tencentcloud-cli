**Example 1: xx**

xx

Input: 

```
tccli dsgc DecribeSuggestRiskLevelMatrix --cli-unfold-argument  \
    --DspaId abc \
    --SensitiveLevelList.0.Name abc \
    --SensitiveLevelList.0.Id 0 \
    --SensitiveLevelList.0.Score 0 \
    --VulnerabilityLevelList.0.Name abc \
    --VulnerabilityLevelList.0.Id 0 \
    --VulnerabilityLevelList.0.Score 0
```

Output: 
```
{
    "Response": {
        "SuggestRiskLevelMatrix": [
            {
                "RiskLevelMatrix": [
                    {
                        "SensitiveLevel": {
                            "Name": "abc",
                            "Id": 0,
                            "Score": 0
                        },
                        "VulnerabilityLevel": {
                            "Name": "abc",
                            "Id": 0,
                            "Score": 0
                        },
                        "RiskName": "abc",
                        "RiskScore": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

