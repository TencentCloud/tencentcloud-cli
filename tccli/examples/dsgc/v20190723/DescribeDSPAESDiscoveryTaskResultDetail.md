**Example 1: xx**

查询es的分类分级扫描任务结果详情

Input: 

```
tccli dsgc DescribeDSPAESDiscoveryTaskResultDetail --cli-unfold-argument  \
    --DspaId abc \
    --TaskId 0 \
    --ComplianceId 0 \
    --CategoryIdList 0 \
    --LevelId 0 \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskId": "abc",
                "FieldName": "abc",
                "RuleId": 0,
                "RuleName": "abc",
                "CategoryId": 0,
                "CategoryName": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

