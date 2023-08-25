**Example 1: xx**

xx

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskTemplateDetail --cli-unfold-argument  \
    --DspaId abc \
    --TemplateId 0 \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TemplateId": 0,
        "TemplateName": "abc",
        "TemplateDescription": "abc",
        "RiskLevelId": 0,
        "RiskLevelName": "abc",
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
                ]
            }
        ],
        "TotalCount": 0,
        "TaskCitations": 0,
        "RequestId": "abc"
    }
}
```

