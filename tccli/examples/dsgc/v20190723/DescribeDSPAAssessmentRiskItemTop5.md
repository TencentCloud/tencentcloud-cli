**Example 1: 风险分类TOP5统计**

风险分类TOP5统计

Input: 

```
tccli dsgc DescribeDSPAAssessmentRiskItemTop5 --cli-unfold-argument  \
    --DspaId dspa-92aabacd
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "RiskNum": 38,
                "ItemName": "数据库账号和权限评估"
            },
            {
                "RiskNum": 9,
                "ItemName": "数据库风险配置"
            },
            {
                "RiskNum": 5,
                "ItemName": "数据库明文存储敏感信息"
            },
            {
                "RiskNum": 1,
                "ItemName": "aksk泄露风险"
            }
        ],
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

