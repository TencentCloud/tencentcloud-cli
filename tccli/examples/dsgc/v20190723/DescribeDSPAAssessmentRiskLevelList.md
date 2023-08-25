**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskLevelList --cli-unfold-argument  \
    --DspaId abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RiskLevelList": [
            {
                "Id": 0,
                "RiskLevelName": "abc",
                "RiskLevelDescription": "abc",
                "IdentifyComplianceName": "abc",
                "Type": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

