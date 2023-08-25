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
        "TotalCount": 1,
        "Items": [
            {
                "TaskId": "task-otxxxwu3",
                "TaskName": "test_03",
                "BusinessName": "tx",
                "BusinessDept": "tx",
                "BusinessOwner": "tx",
                "TemplateId": "template-00000000",
                "TemplateName": "系统基础自动化评估模板",
                "ComplianceGroupId": 1,
                "ComplianceGroupName": "通用规则集",
                "ControlItemCount": 0,
                "RiskCount": 1,
                "RiskCountInfoList": [
                    {
                        "RiskLevel": "高",
                        "Count": 0
                    },
                    {
                        "RiskLevel": "中",
                        "Count": 1
                    },
                    {
                        "RiskLevel": "低",
                        "Count": 0
                    }
                ],
                "FinishedTime": "2022-06-27 20:34:07",
                "CreatedTime": "2022-06-27 20:33:45",
                "Status": "finished",
                "DiscoveryCondition": {
                    "RDBInstances": null,
                    "COSInstances": [
                        {
                            "DataSourceId": "cos-af8bd626a70111239f744bb623a19aba82ff29e7",
                            "BucketName": "casb-1265441191",
                            "ResourceRegion": "ap-guangzhou"
                        },
                        {
                            "DataSourceId": "cos-68437d4a123451387fa35fb72d931d97763f076f",
                            "BucketName": "casb-automated-1654641191",
                            "ResourceRegion": "ap-guangzhou"
                        }
                    ]
                },
                "ErrorInfo": "DiscoveryTask Error,DiscoveryTaskName:COS-NDkxMzYy-对应评估任务-test_03"
            }
        ],
        "RequestId": "9a9f5c32-95ab-4130-ae37-047cde38b943"
    }
}
```

