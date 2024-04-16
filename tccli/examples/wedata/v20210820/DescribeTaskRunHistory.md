**Example 1: 分页查询任务运行历史示例**

分页查询任务运行历史

Input: 

```
tccli wedata DescribeTaskRunHistory --cli-unfold-argument  \
    --ProjectId 1531609696090365952 \
    --SearchCondition.CycleList D \
    --SearchCondition.DateFrom 2024-04-09 22:49:50 \
    --SearchCondition.DateTo 2024-04-12 10:35:30 \
    --SearchCondition.Instance.ExecutionSpace CYCLIC \
    --SearchCondition.Instance.ProductName DATA_DEV \
    --SearchCondition.Keyword 20240306160150595 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AvgCostTime": 0,
                    "CostMillisecond": 0,
                    "CostTime": "00:00:00.000",
                    "CreateTime": "2024-04-10 00:00:17",
                    "CurRunDate": "2024-04-10 00:00:00",
                    "CycleType": "DAY_CYCLE",
                    "DependenceFulfillTime": "2024-04-10 23:35:46",
                    "DependencyRel": null,
                    "DoFlag": 0,
                    "EndTime": "2024-04-10 23:35:56",
                    "ErrorDesc": "Dependency check failed at 202403061595_2024-04-10 00:00:00 with reason: Can not find the correct state task 20240300150595",
                    "ExecutionSpace": "CYCLIC",
                    "ExecutorGroupId": null,
                    "ExecutorGroupName": null,
                    "FirstDependenceFulfillTime": "2024-04-10 00:01:06",
                    "FirstRunTime": null,
                    "FirstStartTime": null,
                    "FirstSubmitTime": null,
                    "FolderId": null,
                    "FolderName": null,
                    "IgnoreEvent": true,
                    "InCharge": "kaiqidong",
                    "InstanceKey": "20240306595_2024-04-10 00:00:00",
                    "InstanceLifeCycleOpsDto": null,
                    "LastLog": "Had been enforce kill",
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2024-04-10 23:41:15",
                    "MaxCostTime": 0,
                    "MinCostTime": 0,
                    "NextCurDate": "2024-04-11 00:00:00",
                    "OwnerId": "",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1531609960952",
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "RedoFlag": 0,
                    "RelatedInstanceList": null,
                    "RelatedInstanceSize": 0,
                    "ResourceGroup": "202307220519606",
                    "ResourceInstanceId": "any",
                    "RetryAttempts": 0,
                    "RunPriority": 6,
                    "RuntimeBroker": null,
                    "SchedulerDateTime": "2024-04-10 00:00:00",
                    "SchedulerDesc": null,
                    "SonList": null,
                    "StartTime": null,
                    "State": "EXPIRED",
                    "TaskId": "2024030616015",
                    "TaskName": "testsasdfas",
                    "TaskType": {
                        "TypeDesc": "JDBC SQL",
                        "TypeId": 21,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "TotalRunNum": 0,
                    "Tries": 0,
                    "TryLimit": 5,
                    "UserId": "",
                    "VirtualFlag": null,
                    "WorkflowId": "7e602618-56e1-11ee-8d13-a272",
                    "WorkflowName": "20230919_release_check",
                    "YarnQueue": null
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "aeba8b49-202f-4252-a623-2402691f2c7b"
    }
}
```

