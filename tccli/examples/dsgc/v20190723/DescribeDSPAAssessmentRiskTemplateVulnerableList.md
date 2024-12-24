**Example 1: 查询风险模板中的脆弱项配置**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskTemplateVulnerableList --cli-unfold-argument  \
    --DspaId dspa-8asdac1a \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RiskItemList": [
            {
                "Id": 38,
                "Level": "high",
                "Description": "服务端口公网开放",
                "RiskType": "policy_risk",
                "ReferTemplateCount": 0,
                "ReferTemplateList": null,
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
        "TotalCount": 0,
        "RequestId": "c42f9bd0-8843-4c3a-f0f2-3d1d50d19c5d"
    }
}
```

