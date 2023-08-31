**Example 1: xx**

查询风险面的分布详情

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskSideDistributed --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0
```

Output: 
```
{
    "Response": {
        "RiskSideDistributed": [
            {
                "AssessmentRiskSide": {
                    "Key": "abc",
                    "Value": 0
                },
                "AssessmentRisk": [
                    {
                        "Key": "abc",
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

