**Example 1: 风险面列表**

查询风险面的列表

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskSideList --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --TemplateId 100118
```

Output: 
```
{
    "Response": {
        "RiskSideItmeList": [
            {
                "Key": "cloudstorage_security",
                "Value": 3
            }
        ],
        "RequestId": "test-001"
    }
}
```

