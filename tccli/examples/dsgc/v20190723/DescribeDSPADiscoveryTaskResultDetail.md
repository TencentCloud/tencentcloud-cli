**Example 1: 获取分类分级任务结果详情**

xx

Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskResultDetail --cli-unfold-argument  \
    --DbResultId 1 \
    --ComplianceId 1 \
    --TableName test \
    --DspaId dspa-001 \
    --Limit 1 \
    --TaskId 1 \
    --Offset 0 \
    --DbName db1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskId": 0,
                "FieldResultId": 0,
                "TableName": "abc",
                "FieldName": "abc",
                "CategoryId": 0,
                "CategoryName": "abc",
                "LevelId": 0,
                "LevelName": "abc",
                "RuleName": "abc",
                "RuleId": 0,
                "LevelRiskScore": 0,
                "SafeGuard": {
                    "Encrypt": "abc",
                    "Desensitization": "abc"
                },
                "CategoryFullPath": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

