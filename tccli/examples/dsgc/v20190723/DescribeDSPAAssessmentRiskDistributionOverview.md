**Example 1: 查询风险分布数据**



Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskDistributionOverview --cli-unfold-argument  \
    --DspaId dspa-8uscas3a \
    --TemplateId 1
```

Output: 
```
{
    "Response": {
        "RiskTypeDistribution": [
            {
                "Key": "config_risk",
                "Value": 10
            }
        ],
        "RiskDetailDistribution": [
            {
                "Key": "数据库参数安全配置-低风险",
                "Value": 10
            }
        ],
        "RiskAssetsDistribution": [
            {
                "Key": "cdb-234nnas1",
                "Value": 10
            }
        ],
        "RequestId": "abc"
    }
}
```

