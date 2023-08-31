**Example 1: 风险面列表**

查询风险面的列表

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskSideList --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0
```

Output: 
```
{
    "Response": {
        "RiskSideItmeList": [
            {
                "Key": "abc",
                "Value": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

