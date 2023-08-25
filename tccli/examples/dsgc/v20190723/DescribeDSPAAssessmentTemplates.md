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
        "TotalCount": 1,
        "Items": [
            {
                "TemplateId": "template-00000000",
                "TemplateName": "系统基础自动化评估模板",
                "Description": "系统基础自动化评估模板",
                "Source": "system",
                "UseType": "auto",
                "CreatedTime": "2022-04-14 18:52:43",
                "ControlItemCount": 4,
                "AppliedItemCount": 4,
                "Status": "launched"
            }
        ],
        "RequestId": "9a9f5c32-95ab-4130-ae37-047cde38b943"
    }
}
```

