**Example 1: 查询最新的风险详情列表数据**

查询最新的风险详情列表数据

Input: 

```
tccli dsgc DescribeDSPAAssessmentLatestRiskList --cli-unfold-argument  \
    --DspaId dspa-a2c3d4e3 \
    --TemplateId 2 \
    --Limit 0 \
    --Offset 10 \
    --DataSourceId mariadb-a1b2c3d4 \
    --RiskType policy_risk \
    --ControlItemId 82 \
    --Status 0 \
    --BeginTime 2022/10/17 \
    --EndTime 2022/10/17 \
    --RiskLevel high
```

Output: 
```
{
    "Response": {
        "LatestRiskList": [
            {
                "Id": 1,
                "DataSourceId": "mariadb-c57d871c",
                "DataSourceName": "订单数据库",
                "DataSourceType": "mariadb",
                "AssetName": "casb001",
                "RiskType": "privilege_risk",
                "RiskName": "数据库账号未配置最小权限",
                "RiskLevel": "high",
                "RiskDescription": "如果数据库账号权限过大可能会导致数据泄露或数据被篡改。",
                "SuggestAction": "遵循最小权限原则，只为每个账号分配其需要的权限",
                "APIRiskLinkURL": "https://console.cloud.tencent.com/dsc/risks",
                "Status": 0,
                "SecurityProduct": [
                    {
                        "ProductName": "数据安全审计",
                        "ReferUrl": "https://console.cloud.tencent.com/cds/overview"
                    }
                ],
                "ScanTime": "2022-10-17 10:04:46",
                "LastProcessTime": "2022-10-17 10:04:46",
                "IdentifyComplianceId": 1,
                "ItemSubType": "db_sensitive_data"
            }
        ],
        "TotalCount": 1,
        "RequestId": "a3c46565-737b-419e-921d-7a38ebb50771"
    }
}
```

