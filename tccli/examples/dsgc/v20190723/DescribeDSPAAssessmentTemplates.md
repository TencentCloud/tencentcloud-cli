**Example 1: 获取DSPA评估模板列表**



Input: 

```
tccli dsgc DescribeDSPAAssessmentTemplates --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "Id": 0,
                "TemplateId": "abc",
                "TemplateName": "abc",
                "Description": "abc",
                "Source": "abc",
                "UseType": "abc",
                "CreatedTime": "abc",
                "ControlItemCount": 0,
                "AppliedItemCount": 0,
                "Status": "abc",
                "SupportDataSource": [
                    "abc"
                ],
                "IsASMTemplate": true,
                "IdentifyComplianceId": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

