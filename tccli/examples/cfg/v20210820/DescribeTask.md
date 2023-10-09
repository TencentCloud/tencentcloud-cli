**Example 1: 查询演练任务**



Input: 

```
tccli cfg DescribeTask --cli-unfold-argument  \
    --TaskId 0
```

Output: 
```
{
    "Response": {
        "ReportInfo": null,
        "RequestId": "68da5328-ff1f-4320-92c0-a67e65c8a298",
        "Task": {
            "AlarmPolicy": [],
            "ApmServiceList": [
                {
                    "InstanceId": "test-ins",
                    "RegionId": 1,
                    "ServiceNameList": [
                        "test-service"
                    ]
                }
            ],
            "ApplicationId": "",
            "ApplicationName": "",
            "Tags": [],
            "TaskCreateTime": "2023-10-09 10:55:18",
            "TaskDescription": "测试",
            "TaskEndTime": null,
            "TaskExpect": null,
            "TaskGroups": [
                {
                    "ObjectTypeId": 1,
                    "TaskGroupActions": [
                        {
                            "ActionApiType": 1,
                            "ActionAttribute": 1,
                            "ActionId": 1,
                            "ActionRisk": "高风险",
                            "ActionTitle": "关机（测试）",
                            "ActionType": "平台",
                            "IsExecuteRedo": false,
                            "TaskGroupActionCreateTime": "2023-10-09 10:55:18",
                            "TaskGroupActionCustomConfiguration": "{}",
                            "TaskGroupActionExecuteId": null,
                            "TaskGroupActionExecuteTime": null,
                            "TaskGroupActionGeneralConfiguration": "{\"AliasTitle\": \"\", \"PreTimeWait\": 0, \"ActionTimeout\": 1800, \"AfterTimeWait\": 0}",
                            "TaskGroupActionId": 13785,
                            "TaskGroupActionOrder": 1,
                            "TaskGroupActionRandomId": 457181,
                            "TaskGroupActionRecoverId": 355514,
                            "TaskGroupActionStatus": 2001,
                            "TaskGroupActionStatusType": 0,
                            "TaskGroupActionUpdateTime": "2023-10-09 10:55:18",
                            "TaskGroupInstances": []
                        },
                        {
                            "ActionApiType": 1,
                            "ActionAttribute": 2,
                            "ActionId": 2,
                            "ActionRisk": "高风险",
                            "ActionTitle": "开机",
                            "ActionType": "平台",
                            "IsExecuteRedo": false,
                            "TaskGroupActionCreateTime": "2023-10-09 10:55:18",
                            "TaskGroupActionCustomConfiguration": "{}",
                            "TaskGroupActionExecuteId": 457181,
                            "TaskGroupActionExecuteTime": null,
                            "TaskGroupActionGeneralConfiguration": "{\"PreTimeWait\": 0, \"ActionTimeout\": 1800, \"AfterTimeWait\": 0}",
                            "TaskGroupActionId": 13786,
                            "TaskGroupActionOrder": 2,
                            "TaskGroupActionRandomId": 355514,
                            "TaskGroupActionRecoverId": null,
                            "TaskGroupActionStatus": 2001,
                            "TaskGroupActionStatusType": 0,
                            "TaskGroupActionUpdateTime": "2023-10-09 10:55:18",
                            "TaskGroupInstances": []
                        }
                    ],
                    "TaskGroupCreateTime": "2023-10-09 10:55:18",
                    "TaskGroupDescription": "1",
                    "TaskGroupDiscardInstanceList": [],
                    "TaskGroupId": 6454,
                    "TaskGroupInstanceList": [
                        "ins-knq6h3r8",
                        "ins-61eitwrk",
                        "ins-d2e45nba"
                    ],
                    "TaskGroupInstancesExecuteRule": [
                        {
                            "TaskGroupInstancesExecuteMode": 3,
                            "TaskGroupInstancesExecuteNum": 2,
                            "TaskGroupInstancesExecutePercent": 100
                        }
                    ],
                    "TaskGroupMode": 1,
                    "TaskGroupOrder": 1,
                    "TaskGroupSelectedInstanceList": [],
                    "TaskGroupTitle": "1",
                    "TaskGroupUpdateTime": "2023-10-09 10:55:18"
                }
            ],
            "TaskId": 5417,
            "TaskMode": 1,
            "TaskMonitors": [
                {
                    "InstancesIds": [
                        "ins-knq6h3r8",
                        "ins-61eitwrk",
                        "ins-d2e45nba"
                    ],
                    "MetricChineseName": "CPU使用率",
                    "MetricId": 614,
                    "MetricName": "CpuUsage",
                    "TaskMonitorId": 5850,
                    "TaskMonitorObjectTypeId": 1,
                    "Unit": "%"
                }
            ],
            "TaskOwnerUin": "700000174829",
            "TaskPauseDuration": 60,
            "TaskPlanId": null,
            "TaskPlanTitle": null,
            "TaskPolicy": null,
            "TaskProtectStrategy": null,
            "TaskRegionId": 1,
            "TaskStartTime": null,
            "TaskStatus": 1001,
            "TaskStatusType": 0,
            "TaskSummary": null,
            "TaskTag": "",
            "TaskTitle": "测试",
            "TaskUpdateTime": "2023-10-09 10:55:18"
        }
    }
}
```

