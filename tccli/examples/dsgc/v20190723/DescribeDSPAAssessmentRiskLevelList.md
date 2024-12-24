**Example 1: 查询风险等级的列表**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskLevelList --cli-unfold-argument  \
    --DspaId dspa-90zcads3 \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RiskLevelList": [
            {
                "Id": 1,
                "RiskLevelName": "默认风险级别",
                "RiskLevelDescription": "自动化测试，勿删",
                "IdentifyComplianceName": "通用规则集",
                "Type": "system"
            }
        ],
        "RequestId": "61ad9ba2-83b7-48cd-aa70-e140525770c8"
    }
}
```

