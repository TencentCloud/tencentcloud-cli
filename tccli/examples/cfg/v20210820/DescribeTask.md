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

