**Example 1: 查看评估模板详情**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskTemplateDetail --cli-unfold-argument  \
    --DspaId dspa-12bhjzx8 \
    --TemplateId 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RiskLevelName": "默认风险级别",
        "RiskItemList": [
            {
                "Id": 38,
                "Level": "high",
                "Description": "服务端口公网开放",
                "RiskType": "policy_risk",
                "ReferTemplateCount": 0,
                "ReferTemplateList": [
                    {
                        "TemplateId": 10,
                        "TemplateName": "风险模版"
                    }
                ],
                "SupportDataSource": [
                    "cynosdb",
                    "dcdb",
                    "cdb",
                    "mariadb",
                    "postgres",
                    "es",
                    "mysql_like_proto",
                    "postgre_like_proto",
                    "mongo_like_proto",
                    "es_like_proto",
                    "mssql_like_proto",
                    "oracle_like_proto",
                    "cynosdbmysql"
                ],
                "RiskName": "服务端口公网开放",
                "RiskSide": "database_security"
            }
        ],
        "TotalCount": 1,
        "TemplateId": 1,
        "TemplateName": "当前模版",
        "TemplateDescription": "模版描述",
        "RiskLevelId": 1,
        "TaskCitations": 1,
        "RequestId": "06b2b669-75cc-4047-a36f-80987f12f6b5"
    }
}
```

