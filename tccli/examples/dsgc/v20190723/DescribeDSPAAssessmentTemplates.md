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
                "Id": 2,
                "TemplateId": "template-00000002",
                "TemplateName": "系统基础评估模板",
                "Description": "自动化测试，勿删",
                "Source": "system",
                "UseType": "auto",
                "CreatedTime": "2023-05-13 14:01:45",
                "ControlItemCount": 194,
                "AppliedItemCount": 63,
                "Status": "launched",
                "SupportDataSource": [
                    "mysql",
                    "pgsql",
                    "mongodb",
                    "oracle",
                    "mssql",
                    "es",
                    "cos",
                    "cam",
                    "db2",
                    "apigateway"
                ],
                "IsASMTemplate": false,
                "IdentifyComplianceId": 1
            }
        ],
        "RequestId": "0db4a846-ad6e-4446-b393-6d5169c88778"
    }
}
```

