**Example 1: 获取任务列表**



Input: 

```
tccli wedata DescribeOperateOpsTasks --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AllowRedoType": "ALL",
                    "BrokerIp": null,
                    "ClusterId": null,
                    "CreateTime": "2024-07-08 17:15:11",
                    "Creator": "carlshi",
                    "Crontab": null,
                    "CrontabExpression": null,
                    "CycleNum": 1,
                    "CycleStep": null,
                    "CycleType": null,
                    "CycleUnit": "D",
                    "DLCResourceConfig": null,
                    "DelayTime": 0,
                    "DependencyRel": null,
                    "DependencyWorkflow": null,
                    "EndDate": "2099-12-31 23:59:59",
                    "EndTime": null,
                    "EventListenerConfig": null,
                    "EventListenerInfos": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": "23:59",
                    "ExecutionStartTime": "00:00",
                    "ExecutionTTL": -1,
                    "ExecutorGroupId": "20221219061532357712",
                    "ExecutorGroupName": "dev_inlong_v9_1219_03",
                    "ExtResourceFlag": null,
                    "FirstRunTime": "2024-07-08 00:00:00",
                    "FirstSubmitTime": "2024-09-05 12:25:03",
                    "FolderId": "8a098d2e-3cff-11ef-8ec8-b8599f277de5",
                    "FolderName": "carlshi",
                    "InCharge": ";Wedata开发测试专用;",
                    "InChargeId": null,
                    "InitStrategy": "T+0",
                    "InstanceInitStrategy": null,
                    "LastSchedulerCommitTime": "2024-09-05 12:25:03",
                    "LastUpdate": "2025-08-13 11:47:42",
                    "Layer": null,
                    "LeftCoordinate": 752,
                    "MaxDateTime": null,
                    "MinDateTime": null,
                    "NewParentTaskInfos": null,
                    "NormalizedJobStartTime": null,
                    "Notes": "",
                    "OwnId": null,
                    "OwnerId": "100028448903",
                    "ProductName": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目_new2",
                    "RealWorkflowId": null,
                    "ResourceGroup": null,
                    "RetryAble": 1,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "ScheduleDesc": "每天00:00执行一次(UTC+8)",
                    "SchedulerDesc": null,
                    "ScriptInfo": null,
                    "SelfDepend": "parallel",
                    "SelfWorkFlowDependType": "no",
                    "ShowWorkflow": false,
                    "SourceServiceId": "9638",
                    "SourceServiceType": "mysql",
                    "StartDate": "2024-07-08 00:00:00",
                    "StartTime": null,
                    "StartupTime": null,
                    "Status": "F",
                    "TargetServiceId": "9638",
                    "TargetServiceType": "mysql",
                    "TaskAction": "",
                    "TaskExtInfo": null,
                    "TaskId": "20240708171511541",
                    "TaskLinkInfo": null,
                    "TaskName": "test11212",
                    "TaskType": null,
                    "TaskTypeDesc": "Offline Synchronization",
                    "TaskTypeId": 26,
                    "TenantId": "1315051789",
                    "TopCoordinate": 211,
                    "TryLimit": 5,
                    "UpdateTime": null,
                    "UpdateUser": "yaofuwang",
                    "UpdateUserId": "100036013191",
                    "UserId": "100028448903",
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "05239aaa-325b-4d12-9c86-db4358ef64ce",
                    "WorkflowName": "test12234",
                    "YarnQueue": null
                }
            ],
            "PageCount": 1099,
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1099,
            "TotalPage": 1099
        },
        "RequestId": "ecfdec6f-dacd-434c-8660-fee3b8de316e"
    }
}
```

