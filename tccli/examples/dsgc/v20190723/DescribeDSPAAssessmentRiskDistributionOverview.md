**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDistributionOverview --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0
```

Output: 
```
{
    "Response": {
        "RiskTypeDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "RiskDetailDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "RiskAssetsDistribution": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

