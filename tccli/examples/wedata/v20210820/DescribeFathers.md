**Example 1: test**

test

Input: 

```
tccli wedata DescribeFathers --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageIndex 1 \
    --PageSize 100 \
    --SearchCondition.Instance.TaskId 20230313145623119 \
    --SearchCondition.Instance.CurRunDate 2023-03-13 14:55:53
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AvgCostTime": null,
                    "CostMillisecond": 2000,
                    "CostTime": "00:00:02.000",
                    "CreateTime": "2023-03-13 14:56:11",
                    "CurRunDate": "2023-03-13 14:55:53",
                    "CycleType": "ONEOFF_CYCLE",
                    "DependenceFulfillTime": "2023-03-20 21:18:51",
                    "DependencyRel": null,
                    "DoFlag": 0,
                    "EndTime": "2023-03-20 21:18:20",
                    "ErrorDesc": "",
                    "ExecutionSpace": "CYCLIC",
                    "FirstDependenceFulfillTime": "2023-03-20 21:18:51",
                    "FirstRunTime": null,
                    "FirstStartTime": null,
                    "FirstSubmitTime": null,
                    "FolderId": "cc31c16e-8743-11ed-8909-bc97e105ba60",
                    "FolderName": "stackxchen",
                    "IgnoreEvent": true,
                    "InCharge": "stackxchen",
                    "LastLog": "Had been kill",
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2023-03-20 21:19:02",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2023-03-13 14:55:53",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": null,
                    "RedoFlag": 1,
                    "ResourceGroup": "20221229154930684210",
                    "ResourceInstanceId": "any",
                    "RunPriority": 6,
                    "RuntimeBroker": "ins-6m3r7n1h",
                    "SchedulerDateTime": "2023-03-13 14:55:53",
                    "SchedulerDesc": "2023年03月13日 14:55:53执行",
                    "SonList": null,
                    "StartTime": "2023-03-20 21:18:18",
                    "State": "EXPIRED",
                    "TaskId": "20230313145539749",
                    "TaskName": "parent_task",
                    "TaskType": {
                        "TypeDesc": "Shell",
                        "TypeId": 35,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "TotalRunNum": 0,
                    "Tries": 0,
                    "TryLimit": 5,
                    "VirtualFlag": null,
                    "WorkflowId": "d3398ce9-8743-11ed-8909-bc97e105ba60",
                    "WorkflowName": "flow_01",
                    "YarnQueue": null
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 100,
            "TotalCount": 1,
            "TotalPage": 0
        },
        "RequestId": "2df24e34-ec63-442d-afdc-b0723442f1cf"
    }
}
```

