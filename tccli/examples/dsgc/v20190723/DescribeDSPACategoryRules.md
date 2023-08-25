**Example 1: 获取合规组分类规则信息**

获取合规组分类规则信息

Input: 

```
tccli dsgc DescribeDSPACategoryRules --cli-unfold-argument  \
    --DspaId dspa-001 \
    --CategoryId 1 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "CategoryRules": [
            {
                "Id": 1,
                "CategoryId": 165,
                "RuleId": 1,
                "RuleName": "银行卡",
                "LevelId": 5,
                "LevelName": "S3"
            },
            {
                "Id": 2,
                "CategoryId": 165,
                "RuleId": 2,
                "RuleName": "信用卡",
                "LevelId": 6,
                "LevelName": "S2"
            }
        ]
    }
}
```

