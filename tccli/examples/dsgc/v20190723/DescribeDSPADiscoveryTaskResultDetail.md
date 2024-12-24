**Example 1: 获取分类分级任务结果详情**

获取分类分级任务结果详情

Input: 

```
tccli dsgc DescribeDSPADiscoveryTaskResultDetail --cli-unfold-argument  \
    --DbResultId 1 \
    --ComplianceId 2 \
    --TableName tb_01 \
    --DspaId dspa-98ahs23n  \
    --Limit 10 \
    --TaskId 105 \
    --Offset 0 \
    --DbName db1
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "TaskId": 105,
                "FieldResultId": 1,
                "TableName": "tb_01",
                "FieldName": "fidld_01",
                "CategoryId": 103,
                "CategoryName": "个人身份信息",
                "LevelId": 112,
                "LevelName": "高",
                "RuleName": "身份证",
                "RuleId": 126,
                "LevelRiskScore": 10,
                "SafeGuard": {
                    "Encrypt": "UNSET",
                    "Desensitization": "UNSET"
                },
                "CategoryFullPath": "[\"个人基本信息\"]"
            }
        ],
        "TotalCount": 1,
        "RequestId": "1f1765cf-c01a-4a93-95b2-99108f4aa04f"
    }
}
```

