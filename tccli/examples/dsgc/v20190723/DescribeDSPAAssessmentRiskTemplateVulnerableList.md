**Example 1: 示例**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskTemplateVulnerableList --cli-unfold-argument  \
    --DspaId abc \
    --RiskType abc \
    --RiskName abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RiskItemList": [
            {
                "Id": 0,
                "RiskName": "abc",
                "Level": "abc",
                "Description": "abc",
                "RiskType": "abc",
                "ReferTemplateCount": 0,
                "SupportDataSource": [
                    "abc"
                ],
                "RiskSide": "abc",
                "ReferTemplateList": [
                    {
                        "TemplateId": 0,
                        "TemplateName": "abc"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

