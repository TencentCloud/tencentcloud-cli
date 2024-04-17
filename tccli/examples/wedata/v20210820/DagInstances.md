**Example 1: 拉取dag实例**

拉取dag实例

Input: 

```
tccli wedata DagInstances --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageIndex 1 \
    --PageSize 10000 \
    --SearchCondition.Instance.TaskId 20230313145623119 \
    --SearchCondition.Instance.CurRunDate 2023-03-13 14:55:53 \
    --SearchCondition.DagType 1 \
    --SearchCondition.DagDependent 3 \
    --SearchCondition.DagDepth 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "InstanceKey": "20230313145623119_2023-03-13 14:55:53",
                    "AvgCostTime": null,
                    "CostMillisecond": null,
                    "CostTime": "00:00:00.000",
                    "CreateTime": "2023-03-13 14:57:01",
                    "CurRunDate": "2023-03-13 14:55:53",
                    "CycleType": "ONEOFF_CYCLE",
                    "DependenceFulfillTime": "2023-03-20 21:15:45",
                    "DependencyRel": null,
                    "DoFlag": 0,
                    "EndTime": "2023-03-20 21:16:00",
                    "ErrorDesc": "Dependency check failed at 2023-03-20T21:21:13.007+08:00 with reason: task 20230313145623119 's parent task instance failed: 20230313145539749 2023-03-13 14:55:53; parent instance failed num:1;relationShip:AND",
                    "ExecutionSpace": "CYCLIC",
                    "FirstDependenceFulfillTime": "2023-03-20 21:15:45",
                    "FirstRunTime": null,
                    "FirstStartTime": null,
                    "FirstSubmitTime": null,
                    "FolderId": null,
                    "FolderName": null,
                    "IgnoreEvent": true,
                    "InCharge": "stackxchen",
                    "LastLog": null,
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2023-03-20 21:21:14",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2023-03-13 14:55:53",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "RedoFlag": 1,
                    "ResourceGroup": "20221229154930684210",
                    "ResourceInstanceId": "any",
                    "RunPriority": 6,
                    "RuntimeBroker": "ins-6m3r7n1h",
                    "SchedulerDateTime": "2023-03-13 14:55:53",
                    "SchedulerDesc": null,
                    "SonList": "[&&&\"TaskId\":\"20230313145539749\",\"TaskName\":\"parent_task\",\"WorkflowId\":\"d3398ce9-8743-11ed-8909-bc97e105ba60\",\"WorkflowName\":\"flow_01\",\"InCharge\":\"stackxchen\",\"CycleType\":\"ONEOFF_CYCLE\",\"CurRunDate\":\"2023-03-13 14:55:53\",\"NextCurDate\":\"2023-03-13 14:55:53\",\"RunPriority\":6,\"TryLimit\":5,\"Tries\":0,\"TotalRunNum\":0,\"DoFlag\":0,\"RedoFlag\":1,\"State\":\"EXPIRED\",\"RuntimeBroker\":\"ins-6m3r7n1h\",\"ErrorDesc\":\"\",\"TaskType\":&&&\"typeDesc\":\"Shell\",\"typeId\":35,\"typeSort\":\"数据计算\"},\"DependenceFulfillTime\":\"2023-03-20 21:18:51\",\"FirstDependenceFulfillTime\":\"2023-03-20 21:18:51\",\"StartTime\":\"2023-03-20 21:18:18\",\"EndTime\":\"2023-03-20 21:18:20\",\"CostTime\":\"00:00:02.000\",\"CostMillisecond\":2000,\"LastLog\":\"Had been kill\",\"SchedulerDateTime\":\"2023-03-13 14:55:53\",\"LastUpdate\":\"2023-03-20 21:19:02\",\"CreateTime\":\"2023-03-13 14:56:11\",\"ExecutionSpace\":\"CYCLIC\",\"IgnoreEvent\":true,\"VirtualFlag\":false,\"FolderId\":\"cc31c16e-8743-11ed-8909-bc97e105ba60\",\"FolderName\":\"stackxchen\",\"list\":[],\"ProductName\":\"DATA_DEV\",\"ResourceGroup\":\"20221229154930684210\",\"ResourceInstanceId\":\"any\",\"SchedulerDesc\":\"2023年03月13日 14:55:53执行\",\"ProjectIdent\":\"us_dev\",\"ProjectName\":\"调度dev验证项目\",\"TenantId\":\"1315051789\"}]",
                    "StartTime": null,
                    "State": "EVENT_LISTENING",
                    "TaskId": "20230313145623119",
                    "TaskName": "son_task",
                    "TaskType": {
                        "TypeDesc": "Shell",
                        "TypeId": 35,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "TotalRunNum": 0,
                    "Tries": 0,
                    "TryLimit": 5,
                    "VirtualFlag": false,
                    "WorkflowId": "d3398ce9-8743-11ed-8909-bc97e105ba60",
                    "WorkflowName": "flow_01",
                    "YarnQueue": null
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 10000,
            "TotalCount": 1,
            "TotalPage": 0
        },
        "RequestId": "aee4481f-a666-4d70-bcb6-d8b579b46086"
    }
}
```

**Example 2: 获取当前实例的子实例**

获取当前实例的子实例

Input: 

```
tccli wedata DagInstances --cli-unfold-argument  \
    --SearchCondition.Instance.TaskId 20240307211633923 \
    --SearchCondition.Instance.CurRunDate 2024-04-12 00:00:00 \
    --SearchCondition.DagType 2 \
    --SearchCondition.DagDependent 3 \
    --SearchCondition.DagDepth 1 \
    --ProjectId 1492511691706699776 \
    --PageIndex 1 \
    --PageSize 10000
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AvgCostTime": null,
                    "CostMillisecond": null,
                    "CostTime": "00:02:02.000",
                    "CreateTime": "2024-04-12 14:56:56",
                    "CurRunDate": "2024-04-12 00:00:00",
                    "CycleType": "CRONTAB_CYCLE",
                    "DependenceFulfillTime": "2024-04-12 14:56:56",
                    "DependencyRel": null,
                    "DoFlag": 1,
                    "EndTime": "2024-04-12 14:59:05",
                    "ErrorDesc": "",
                    "ExecutionSpace": "CYCLIC",
                    "ExecutorGroupId": null,
                    "ExecutorGroupName": null,
                    "FirstDependenceFulfillTime": "2024-04-12 14:56:56",
                    "FirstRunTime": null,
                    "FirstStartTime": "2024-04-12 14:57:03",
                    "FirstSubmitTime": null,
                    "FolderId": null,
                    "FolderName": null,
                    "IgnoreEvent": true,
                    "InCharge": "micofywang",
                    "InstanceKey": "20240307211633923_2024-04-12 00:00:00",
                    "InstanceLifeCycleOpsDto": null,
                    "LastLog": null,
                    "LastSchedulerDateTime": null,
                    "LastUpdate": "2024-04-12 14:59:07",
                    "MaxCostTime": null,
                    "MinCostTime": null,
                    "NextCurDate": "2024-04-13 00:00:00",
                    "OwnerId": "100028448903",
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1492511691706699776",
                    "ProjectIdent": "Ryanrliao_DI",
                    "ProjectName": "集成",
                    "RedoFlag": 0,
                    "RelatedInstanceList": null,
                    "RelatedInstanceSize": 0,
                    "ResourceGroup": "20221229172428663695",
                    "ResourceInstanceId": "ins-g8j6pv4f",
                    "RetryAttempts": 0,
                    "RunPriority": 6,
                    "RuntimeBroker": "ins-g8j6pv4f",
                    "SchedulerDateTime": "2024-04-12 00:00:00",
                    "SchedulerDesc": null,
                    "SonList": "[&&&\"TaskId\":\"20240307211852581\",\"TaskName\":\"python_task_failed\",\"WorkflowId\":\"ca1253e8-dc84-11ee-8d13-a4ae120f8272\",\"WorkflowName\":\"mico_wf_test_alarm\",\"InCharge\":\"micofywang\",\"CycleType\":\"CRONTAB_CYCLE\",\"CurRunDate\":\"2024-04-12 00:00:00\",\"NextCurDate\":\"2024-04-13 00:00:00\",\"RunPriority\":6,\"TryLimit\":5,\"Tries\":3,\"TotalRunNum\":3,\"DoFlag\":1,\"RedoFlag\":0,\"State\":\"FAILED\",\"RuntimeBroker\":\"ins-g8j6pv4f\",\"ErrorDesc\":\"\",\"TaskType\":&&&\"TypeDesc\":\"Python\",\"TypeId\":30,\"TypeSort\":\"数据计算\"},\"DependenceFulfillTime\":\"2024-04-12 15:04:32\",\"FirstDependenceFulfillTime\":\"2024-04-12 14:50:09\",\"FirstStartTime\":\"2024-04-12 14:50:23\",\"StartTime\":\"2024-04-12 15:04:37\",\"EndTime\":\"2024-04-12 15:04:40\",\"CostTime\":\"00:00:03.000\",\"CostMillisecond\":3000,\"SchedulerDateTime\":\"2024-04-12 00:00:00\",\"LastUpdate\":\"2024-04-12 15:04:42\",\"CreateTime\":\"2024-04-12 14:50:09\",\"ExecutionSpace\":\"CYCLIC\",\"IgnoreEvent\":true,\"VirtualFlag\":false,\"FolderId\":\"9e954395-d479-11ee-8d13-a4ae120f8272\",\"FolderName\":\"micofywang\",\"list\":[],\"RelatedInstanceSize\":0,\"ProductName\":\"DATA_DEV\",\"ResourceGroup\":\"20221229172428663695\",\"ResourceInstanceId\":\"ins-g8j6pv4f\",\"ProjectId\":\"1492511691706699776\",\"ProjectIdent\":\"Ryanrliao_DI\",\"ProjectName\":\"集成\",\"TenantId\":\"1315051789\",\"OwnerId\":\"100028448903\",\"UserId\":\"100033435965\",\"InstanceKey\":\"20240307211852581_2024-04-12 00:00:00\",\"RetryAttempts\":0}]",
                    "StartTime": "2024-04-12 14:57:03",
                    "State": "COMPLETED",
                    "TaskId": "20240307211633923",
                    "TaskName": "shell_task_timeout_success",
                    "TaskType": {
                        "TypeDesc": "Shell",
                        "TypeId": 35,
                        "TypeSort": "数据计算"
                    },
                    "TenantId": "1315051789",
                    "TotalRunNum": 1,
                    "Tries": 1,
                    "TryLimit": 5,
                    "UserId": "100033435965",
                    "VirtualFlag": false,
                    "WorkflowId": "ca1253e8-dc84-11ee-8d13-a4ae120f8272",
                    "WorkflowName": "mico_wf_test_alarm",
                    "YarnQueue": null
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 10000,
            "TotalCount": 1,
            "TotalPage": 0
        },
        "RequestId": "b71bbdac-8001-4966-b183-a1e4bac8f903"
    }
}
```

