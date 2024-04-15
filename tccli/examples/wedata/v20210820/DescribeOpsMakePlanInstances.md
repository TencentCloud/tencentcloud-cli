**Example 1: 获取补录计划任务实例**

数据补录-获取补录计划任务实例

Input: 

```
tccli wedata DescribeOpsMakePlanInstances --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId 147056160274522xxxx \
    --PlanId e0bed861-0e95-44ca-9d10-28f29752xxxx \
    --TaskId 2023052809431xxxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "TotalPage": 1,
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "TaskId": "2002090216540987",
                    "TaskName": "test_shell_0",
                    "WorkflowId": null,
                    "WorkflowName": null,
                    "InCharge": null,
                    "CycleType": null,
                    "CurRunDate": "2024-04-08 00:00:00",
                    "NextCurDate": null,
                    "RunPriority": 1,
                    "TryLimit": 1,
                    "Tries": 1,
                    "TotalRunNum": 1,
                    "DoFlag": 0,
                    "RedoFlag": 1,
                    "State": "EXPIRED",
                    "RuntimeBroker": null,
                    "ErrorDesc": null,
                    "TaskType": {
                        "TypeDesc": null,
                        "TypeId": 0,
                        "TypeSort": null
                    },
                    "DependenceFulfillTime": null,
                    "FirstDependenceFulfillTime": null,
                    "FirstStartTime": null,
                    "StartTime": null,
                    "EndTime": "2024-04-09 18:21:36",
                    "CostTime": "00:00:00.000",
                    "CostMillisecond": 1,
                    "MaxCostTime": 1,
                    "MinCostTime": 1,
                    "AvgCostTime": 0,
                    "LastLog": null,
                    "SchedulerDateTime": null,
                    "LastSchedulerDateTime": null,
                    "LastUpdate": null,
                    "CreateTime": null,
                    "DependencyRel": null,
                    "ExecutionSpace": null,
                    "IgnoreEvent": true,
                    "VirtualFlag": true,
                    "FolderId": null,
                    "FolderName": null,
                    "SonList": null,
                    "ProductName": null,
                    "ResourceGroup": null,
                    "ResourceInstanceId": null,
                    "YarnQueue": null,
                    "SchedulerDesc": null,
                    "FirstSubmitTime": null,
                    "FirstRunTime": null,
                    "ProjectId": null,
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "TenantId": null,
                    "InstanceKey": null,
                    "ExecutorGroupId": null,
                    "ExecutorGroupName": null,
                    "RelatedInstanceList": [
                        {
                            "TaskId": null,
                            "TaskName": null,
                            "WorkflowId": null,
                            "WorkflowName": null,
                            "InCharge": null,
                            "CycleType": null,
                            "CurRunDate": null,
                            "NextCurDate": null,
                            "RunPriority": 1,
                            "TryLimit": 1,
                            "Tries": 1,
                            "TotalRunNum": 1,
                            "DoFlag": 1,
                            "RedoFlag": 1,
                            "State": null,
                            "RuntimeBroker": null,
                            "ErrorDesc": null,
                            "TaskType": {
                                "TypeDesc": null,
                                "TypeId": 0,
                                "TypeSort": null
                            },
                            "DependenceFulfillTime": null,
                            "FirstDependenceFulfillTime": null,
                            "FirstStartTime": null,
                            "StartTime": "2024-04-09 18:23:48",
                            "EndTime": null,
                            "CostTime": null,
                            "CostMillisecond": 1,
                            "MaxCostTime": 1,
                            "MinCostTime": 1,
                            "AvgCostTime": 0,
                            "LastLog": null,
                            "SchedulerDateTime": null,
                            "LastSchedulerDateTime": null,
                            "LastUpdate": null,
                            "CreateTime": null,
                            "DependencyRel": null,
                            "ExecutionSpace": null,
                            "IgnoreEvent": true,
                            "VirtualFlag": true,
                            "FolderId": null,
                            "FolderName": null,
                            "SonList": null,
                            "ProductName": null,
                            "ResourceGroup": null,
                            "ResourceInstanceId": null,
                            "YarnQueue": null,
                            "SchedulerDesc": null,
                            "FirstSubmitTime": null,
                            "FirstRunTime": null,
                            "ProjectId": null,
                            "ProjectIdent": null,
                            "ProjectName": null,
                            "TenantId": null,
                            "InstanceKey": null,
                            "ExecutorGroupId": null,
                            "ExecutorGroupName": null,
                            "RelatedInstanceList": [
                                {
                                    "TaskId": null,
                                    "TaskName": null,
                                    "WorkflowId": null,
                                    "WorkflowName": null,
                                    "InCharge": null,
                                    "CycleType": null,
                                    "CurRunDate": null,
                                    "NextCurDate": null,
                                    "RunPriority": 1,
                                    "TryLimit": 1,
                                    "Tries": 1,
                                    "TotalRunNum": 1,
                                    "DoFlag": 1,
                                    "RedoFlag": 1,
                                    "State": null,
                                    "RuntimeBroker": null,
                                    "ErrorDesc": null,
                                    "TaskType": {
                                        "TypeDesc": null,
                                        "TypeId": 0,
                                        "TypeSort": null
                                    },
                                    "DependenceFulfillTime": null,
                                    "FirstDependenceFulfillTime": null,
                                    "FirstStartTime": null,
                                    "StartTime": null,
                                    "EndTime": null,
                                    "CostTime": null,
                                    "CostMillisecond": 1,
                                    "MaxCostTime": 1,
                                    "MinCostTime": 1,
                                    "AvgCostTime": 0,
                                    "LastLog": null,
                                    "SchedulerDateTime": null,
                                    "LastSchedulerDateTime": null,
                                    "LastUpdate": null,
                                    "CreateTime": null,
                                    "DependencyRel": null,
                                    "ExecutionSpace": null,
                                    "IgnoreEvent": true,
                                    "VirtualFlag": true,
                                    "FolderId": null,
                                    "FolderName": null,
                                    "SonList": null,
                                    "ProductName": null,
                                    "ResourceGroup": null,
                                    "ResourceInstanceId": null,
                                    "YarnQueue": null,
                                    "SchedulerDesc": null,
                                    "FirstSubmitTime": null,
                                    "FirstRunTime": null,
                                    "ProjectId": null,
                                    "ProjectIdent": null,
                                    "ProjectName": null,
                                    "TenantId": null,
                                    "InstanceKey": null,
                                    "ExecutorGroupId": null,
                                    "ExecutorGroupName": null,
                                    "RelatedInstanceSize": 0,
                                    "OwnerId": null,
                                    "UserId": null,
                                    "InstanceLifeCycleOpsDto": {
                                        "TaskId": null,
                                        "CurRunDate": null,
                                        "LifeRound": 0,
                                        "RunType": null,
                                        "Tries": 0,
                                        "InstanceLifeDetailDtoList": [
                                            {
                                                "State": null,
                                                "StartTime": null,
                                                "DetailState": null,
                                                "EndTime": null
                                            }
                                        ],
                                        "RunnerState": null,
                                        "ErrorDesc": null,
                                        "ErrorCodeLevel": null,
                                        "InstanceLogListOpsDto": {
                                            "TaskId": null,
                                            "CurRunDate": null,
                                            "Tries": null,
                                            "LastUpdate": null,
                                            "BrokerIp": null,
                                            "FileSize": null,
                                            "OriginFileName": null,
                                            "CreateTime": null,
                                            "InstanceLogType": null,
                                            "TaskName": null,
                                            "CostTime": null,
                                            "InstanceStatus": null,
                                            "CodeFileName": null,
                                            "ExtensionInfo": [
                                                {
                                                    "Key": null,
                                                    "Value": null,
                                                    "Description": null
                                                }
                                            ]
                                        },
                                        "InstanceState": null
                                    },
                                    "RetryAttempts": 1
                                }
                            ],
                            "RelatedInstanceSize": 0,
                            "OwnerId": null,
                            "UserId": null,
                            "InstanceLifeCycleOpsDto": {
                                "TaskId": null,
                                "CurRunDate": null,
                                "LifeRound": 0,
                                "RunType": null,
                                "Tries": 0,
                                "InstanceLifeDetailDtoList": [
                                    {
                                        "State": null,
                                        "StartTime": null,
                                        "DetailState": null,
                                        "EndTime": null
                                    }
                                ],
                                "RunnerState": null,
                                "ErrorDesc": null,
                                "ErrorCodeLevel": null,
                                "InstanceLogListOpsDto": {
                                    "TaskId": null,
                                    "CurRunDate": null,
                                    "Tries": null,
                                    "LastUpdate": null,
                                    "BrokerIp": null,
                                    "FileSize": null,
                                    "OriginFileName": null,
                                    "CreateTime": null,
                                    "InstanceLogType": null,
                                    "TaskName": null,
                                    "CostTime": null,
                                    "InstanceStatus": null,
                                    "CodeFileName": null,
                                    "ExtensionInfo": [
                                        {
                                            "Key": null,
                                            "Value": null,
                                            "Description": null
                                        }
                                    ]
                                },
                                "InstanceState": null
                            },
                            "RetryAttempts": 1
                        }
                    ],
                    "RelatedInstanceSize": 0,
                    "OwnerId": null,
                    "UserId": null,
                    "InstanceLifeCycleOpsDto": {
                        "TaskId": null,
                        "CurRunDate": null,
                        "LifeRound": 0,
                        "RunType": null,
                        "Tries": 0,
                        "InstanceLifeDetailDtoList": [
                            {
                                "State": null,
                                "StartTime": null,
                                "DetailState": null,
                                "EndTime": null
                            }
                        ],
                        "RunnerState": null,
                        "ErrorDesc": null,
                        "ErrorCodeLevel": null,
                        "InstanceLogListOpsDto": {
                            "TaskId": null,
                            "CurRunDate": null,
                            "Tries": null,
                            "LastUpdate": null,
                            "BrokerIp": null,
                            "FileSize": null,
                            "OriginFileName": null,
                            "CreateTime": null,
                            "InstanceLogType": null,
                            "TaskName": null,
                            "CostTime": null,
                            "InstanceStatus": null,
                            "CodeFileName": null,
                            "ExtensionInfo": [
                                {
                                    "Key": null,
                                    "Value": null,
                                    "Description": null
                                }
                            ]
                        },
                        "InstanceState": null
                    },
                    "RetryAttempts": 1
                }
            ]
        },
        "RequestId": "123"
    }
}
```

