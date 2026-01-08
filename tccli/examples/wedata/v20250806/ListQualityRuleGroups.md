**Example 1: 查询质量监控列表**



Input: 

```
tccli wedata ListQualityRuleGroups --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Filters.0.Name RuleGroupId \
    --Filters.0.Values 743
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AspectTaskId": "20260105170922315",
                    "CatalogName": "DataLakeCatalog",
                    "ClusterDeployType": null,
                    "CreateTime": "2026-01-05 16:33:34",
                    "CreateUserName": "wenjieyao",
                    "DatabaseId": null,
                    "DatabaseName": "at_dlc_cloud_gz_prod_mc",
                    "DatasourceId": "8860",
                    "DatasourceName": "dlc_DLC_hx756s1y",
                    "DatasourceType": 3,
                    "Description": "create ruleGroup",
                    "EnableRuleCount": 1,
                    "ExecDetail": "20250826201812341",
                    "ExecStrategy": {
                        "CycleStep": 12,
                        "CycleType": "H",
                        "DelayTime": 0,
                        "DlcGroupName": "default-rg-17tv8vfgvy",
                        "EndTime": "2026-01-10 23:59:59",
                        "EngineParam": null,
                        "ExecEngineType": "DLC",
                        "ExecPlan": null,
                        "ExecQueue": "dlc_lina测试勿动",
                        "ExecutorGroupId": "20240222212719833743",
                        "ExecutorGroupName": "qfh_test",
                        "MonitorType": 2,
                        "RuleGroupId": 743,
                        "RuleGroupName": null,
                        "ScheduleTimeZone": "UTC+8",
                        "StartTime": "2026-01-05 00:00:00",
                        "TaskAction": "",
                        "Tasks": [
                            {
                                "InChargeIdList": [
                                    "100043952931"
                                ],
                                "InChargeNameList": [
                                    "brianfzhang"
                                ],
                                "ScheduleTimeZone": null,
                                "TaskId": "20250826201812341",
                                "TaskName": "t01",
                                "TaskType": "1",
                                "WorkflowId": "cd1e7bda-8672-4a6e-b71a-0195084a04f1"
                            }
                        ],
                        "TriggerTypes": [
                            "CYCLE"
                        ]
                    },
                    "GroupType": "DEFAULT",
                    "InstanceId": null,
                    "MonitorStatus": true,
                    "MonitorType": 2,
                    "Name": "mico_rule_group_101",
                    "Permission": true,
                    "PipelineTaskCount": 1,
                    "RuleCount": 1,
                    "RuleGroupId": 743,
                    "SchemaName": null,
                    "Subscription": null,
                    "TableId": null,
                    "TableName": "gee01",
                    "TableOwnerName": null,
                    "TableOwnerUserId": null,
                    "UpdateTime": "2026-01-05 17:09:27"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "70b3c2b2-1e1f-413f-8a88-8fba5dc87996"
    }
}
```

