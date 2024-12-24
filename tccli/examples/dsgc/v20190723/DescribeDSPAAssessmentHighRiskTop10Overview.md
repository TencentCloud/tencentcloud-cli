**Example 1: 查询高风险资产的top10**



Input: 

```
tccli dsgc DescribeDSPAAssessmentHighRiskTop10Overview --cli-unfold-argument  \
    --DspaId dspa-y7asca3a \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "AssetsList": [
            {
                "RiskType": "policy_risk,privilege_risk,",
                "TotalRiskCount": 2,
                "InstanceId": "cdb-5vskvzvn",
                "DataSourceName": "DSGC-功能自动化使用",
                "DataSourceType": "cdb",
                "ResourceRegion": "ap-guangzhou",
                "AssetsName": "automated_sensitivedata_1",
                "HighRiskCount": 2,
                "RiskSide": "database_security"
            }
        ],
        "RequestId": "c42f9bd0-8843-4c3a-f0f2-3d1d50d19c5d"
    }
}
```

