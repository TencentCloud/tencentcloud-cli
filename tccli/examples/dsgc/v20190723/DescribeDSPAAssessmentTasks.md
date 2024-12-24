**Example 1: 获取DSPA评估任务列表**



Input: 

```
tccli dsgc DescribeDSPAAssessmentTasks --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "TaskUid": 11500,
                "TaskId": "task-yji1zgjm",
                "TaskName": "一键评估1109-19491112127",
                "BusinessName": "",
                "BusinessDept": "",
                "BusinessOwner": "",
                "TemplateId": "template-Yzc2Z",
                "TemplateUid": 10171,
                "TemplateName": "身份认证",
                "ComplianceGroupId": 1,
                "ComplianceGroupName": "通用规则集",
                "ControlItemCount": 0,
                "RiskCount": 24,
                "RiskCountInfoList": [
                    {
                        "RiskLevel": "high",
                        "RiskLevelName": "高",
                        "Count": 0
                    },
                    {
                        "RiskLevel": "medium",
                        "RiskLevelName": "中",
                        "Count": 24
                    },
                    {
                        "RiskLevel": "low",
                        "RiskLevelName": "低",
                        "Count": 0
                    }
                ],
                "FinishedTime": "2024-11-09 19:51:33",
                "CreatedTime": "2024-11-09 19:49:11",
                "Status": "finished",
                "DiscoveryCondition": {
                    "RDBInstances": [],
                    "COSInstances": [],
                    "NOSQLInstances": [],
                    "ESInstances": []
                },
                "ErrorInfo": "",
                "ProgressPercent": 100
            }
        ],
        "RequestId": "c9950094-26b3-9163-4fe0-3d60ae5a2d95"
    }
}
```

