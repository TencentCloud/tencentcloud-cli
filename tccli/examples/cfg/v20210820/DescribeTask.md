**Example 1: 查询任务**



Input: 

```
tccli cfg DescribeTask --cli-unfold-argument  \
    --TaskId 309
```

Output: 
```
{
    "Response": {
        "RequestId": "38f8dc62-1213-465d-bc0f-37dfa62230c2",
        "ReportInfo": null,
        "Task": {
            "TaskId": 309,
            "TaskTitle": "123",
            "TaskDescription": "123",
            "TaskTag": "123",
            "TaskStatus": 1001,
            "TaskStatusType": 0,
            "TaskProtectStrategy": null,
            "TaskCreateTime": "2021-09-20 10:27:22",
            "TaskUpdateTime": "2021-09-20 10:27:22",
            "TaskStartTime": null,
            "TaskEndTime": null,
            "TaskExpect": null,
            "TaskSummary": null,
            "TaskMode": 1,
            "TaskRegionId": 1,
            "TaskPauseDuration": 12,
            "TaskOwnerUin": "600000559519",
            "TaskGroups": [
                {
                    "TaskGroupId": 157,
                    "TaskGroupActions": [
                        {
                            "TaskGroupActionId": 185,
                            "TaskGroupInstances": [],
                            "ActionId": 1,
                            "ActionTitle": "关机",
                            "ActionApiType": 1,
                            "ActionRisk": "高风险",
                            "ActionAttribute": 1,
                            "TaskGroupActionOrder": 1,
                            "TaskGroupActionGeneralConfiguration": "{}",
                            "TaskGroupActionCustomConfiguration": "{}",
                            "TaskGroupActionStatus": 2001,
                            "TaskGroupActionStatusType": 0,
                            "TaskGroupActionRandomId": 1,
                            "TaskGroupActionRecoverId": 1,
                            "TaskGroupActionExecuteId": 1,
                            "TaskGroupActionCreateTime": "2021-09-20 10:27:22",
                            "TaskGroupActionUpdateTime": "2021-09-20 10:27:22"
                        }
                    ],
                    "TaskGroupTitle": "123",
                    "TaskGroupDescription": "123",
                    "TaskGroupOrder": 1,
                    "TaskGroupMode": 1,
                    "TaskGroupInstanceList": [
                        "123"
                    ],
                    "ObjectTypeId": 1,
                    "TaskGroupCreateTime": "2021-09-20 10:27:22",
                    "TaskGroupUpdateTime": "2021-09-20 10:27:22"
                }
            ],
            "TaskMonitors": [
                {
                    "TaskMonitorId": 211,
                    "TaskMonitorObjectTypeId": 1,
                    "MetricName": "123",
                    "MetricChineseName": "123",
                    "InstancesIds": [
                        "123"
                    ],
                    "Unit": "aaa"
                }
            ],
            "TaskPolicy": {
                "TaskPolicyIdList": [
                    "123"
                ],
                "TaskPolicyStatus": "未触发",
                "TaskPolicyRule": "123",
                "TaskPolicyDealType": 2
            }
        }
    }
}
```

**Example 2: 2**



Input: 

```
tccli cfg DescribeTask --cli-unfold-argument  \
    --TaskId 3677
```

Output: 
```
{
    "Response": {
        "RequestId": "960e11f4-771b-42f7-8f0d-c73185d203e5",
        "Task": {
            "TaskId": 3677,
            "TaskTitle": "CDB InjectFatal Test",
            "TaskDescription": "CDB InjectFatal Test",
            "TaskTag": "",
            "TaskStatus": 1004,
            "TaskStatusType": 1,
            "TaskProtectStrategy": null,
            "TaskCreateTime": "2022-12-07 10:45:47",
            "TaskUpdateTime": "2022-12-08 19:52:31",
            "TaskStartTime": "2022-12-07 10:48:38",
            "TaskEndTime": "2022-12-08 19:52:31",
            "TaskExpect": 1,
            "TaskSummary": "adgqd",
            "TaskMode": 1,
            "TaskRegionId": 1,
            "TaskPauseDuration": 60,
            "TaskOwnerUin": "700000386736",
            "TaskGroups": [
                {
                    "TaskGroupActions": [
                        {
                            "TaskGroupInstances": [
                                {
                                    "TaskGroupInstanceId": 13455,
                                    "TaskGroupInstanceObjectId": "cdb-k4tpzjr9",
                                    "TaskGroupInstanceStatus": 3003,
                                    "TaskGroupInstanceStatusType": 2,
                                    "TaskGroupInstanceExecuteLog": "实例:cdb-k4tpzjr9, 模拟故障异步任务执行失败. ",
                                    "TaskGroupInstanceStartTime": "2022-12-07 10:48:38",
                                    "TaskGroupInstanceEndTime": "2022-12-07 10:51:06",
                                    "TaskGroupInstanceCreateTime": "2022-12-07 10:47:48",
                                    "TaskGroupInstanceUpdateTime": "2022-12-07 10:51:05",
                                    "TaskGroupInstanceIsRedo": true,
                                    "TaskGroupInstanceExecuteTime": 148
                                }
                            ],
                            "TaskGroupActionId": 9049,
                            "ActionId": 292,
                            "ActionTitle": "CDB主节点故障",
                            "ActionApiType": 1,
                            "ActionType": "平台",
                            "ActionRisk": "高风险",
                            "ActionAttribute": 1,
                            "TaskGroupActionOrder": 1,
                            "TaskGroupActionGeneralConfiguration": "{\"AliasTitle\": \"\", \"PreTimeWait\": 0, \"ActionTimeout\": 1800, \"AfterTimeWait\": 0}",
                            "TaskGroupActionCustomConfiguration": "{}",
                            "TaskGroupActionStatus": 2004,
                            "TaskGroupActionStatusType": 2,
                            "TaskGroupActionRandomId": 988498,
                            "TaskGroupActionRecoverId": null,
                            "TaskGroupActionExecuteId": null,
                            "TaskGroupActionCreateTime": "2022-12-07 10:45:47",
                            "TaskGroupActionUpdateTime": "2022-12-07 10:51:05",
                            "IsExecuteRedo": true,
                            "TaskGroupActionExecuteTime": 148
                        }
                    ],
                    "TaskGroupId": 4193,
                    "TaskGroupTitle": "CDB InjectFatal Test",
                    "TaskGroupDescription": "CDB InjectFatal Test",
                    "TaskGroupOrder": 1,
                    "TaskGroupMode": 1,
                    "TaskGroupInstanceList": [
                        "cdb-k4tpzjr9"
                    ],
                    "ObjectTypeId": 2,
                    "TaskGroupCreateTime": "2022-12-07 10:45:47",
                    "TaskGroupUpdateTime": "2022-12-07 10:45:47"
                }
            ],
            "TaskMonitors": [],
            "TaskPolicy": null,
            "Tags": []
        },
        "ReportInfo": {
            "Stage": 2,
            "CreateTime": "2022-12-14 10:52:06",
            "ExpirationTime": "2022-12-21 10:52:06",
            "Expired": true,
            "CosUrl": "https://chaos-test-1312346585.cos.ap-nanjing.myqcloud.com/task_report/3677/Report.pdf",
            "Log": "0"
        }
    }
}
```

