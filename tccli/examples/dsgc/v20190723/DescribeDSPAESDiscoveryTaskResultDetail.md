**Example 1: 获取ES的分类分级任务结果详情**

查询es的分类分级扫描任务结果详情

Input: 

```
tccli dsgc DescribeDSPAESDiscoveryTaskResultDetail --cli-unfold-argument  \
    --DspaId dspa-9as8cz2s \
    --TaskId 1 \
    --ComplianceId 1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Id": 1,
                "TaskId": 1,
                "FieldName": "name",
                "RuleName": "姓名",
                "RuleId": 14,
                "CategoryId": 103,
                "CategoryName": "个人基本信息",
                "CategoryArr": [
                    "个人基本信息"
                ],
                "LevelId": 2,
                "LevelName": "中",
                "LevelRiskScore": 5
            }
        ],
        "TotalCount": 1,
        "RequestId": "826f0635-b168-52a7-8db9-45b1d46d2c8a"
    }
}
```

