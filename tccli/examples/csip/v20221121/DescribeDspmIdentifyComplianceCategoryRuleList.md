**Example 1: 查询dspm数据识别模板分类关联数据项列表**



Input: 

```
tccli csip DescribeDspmIdentifyComplianceCategoryRuleList --cli-unfold-argument  \
    --ComplianceId 10001 \
    --CategoryId 358 \
    --MemberId mem-12ed1wes \
    --Filter.Limit 100
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "CategoryId": 358,
                "ComplianceId": 10001,
                "LevelId": 1,
                "LevelName": "高",
                "RuleId": 5800,
                "RuleName": "姓名"
            }
        ],
        "TotalCount": 1,
        "RequestId": "91dfb897-62f4-45f4-beda-33a2d8756cc5"
    }
}
```

