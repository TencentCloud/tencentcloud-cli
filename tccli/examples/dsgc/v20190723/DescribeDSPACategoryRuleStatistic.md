**Example 1: 获取分类规则统计信息**

获取分类规则统计信息

Input: 

```
tccli dsgc DescribeDSPACategoryRuleStatistic --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "StatisticSet": [
            {
                "CategoryId": 165,
                "RuleCount": 2
            }
        ]
    }
}
```

