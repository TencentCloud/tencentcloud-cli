**Example 1: 通过taskIds查询task详情列表**

通过taskIds查询task详情列表

Input: 

```
tccli wedata DescribeDependTaskLists --cli-unfold-argument  \
    --TaskIds 'your tasld' \
    --ProjectId your projectId
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BrokerIp": "any",
                "ClusterId": null,
                "CreateTime": "2024-01-03 15:52:36",
                "Creator": "jack",
                "Crontab": null,
                "CrontabExpression": null,
                "CycleNum": null,
                "CycleStep": 1,
                "CycleType": "DAY_CYCLE",
                "CycleUnit": null,
                "DelayTime": 0,
                "DependencyRel": "and",
                "DependencyWorkflow": "no",
                "EndDate": null,
                "EndTime": "2099-12-31 23:59:59",
                "EventListenerConfig": null,
                "EventPublisherConfig": null,
                "ExecutionEndTime": null,
                "ExecutionStartTime": null,
                "ExecutionTTL": -1,
                "ExecutorGroupId": null,
                "ExecutorGroupName": null,
                "FirstRunTime": null,
                "FirstSubmitTime": null,
                "FolderId": null,
                "FolderName": null,
                "InCharge": "v_vyuyudu",
                "InChargeId": "100029071486",
                "InitStrategy": null,
                "InstanceInitStrategy": "T_PLUS_0",
                "LastSchedulerCommitTime": null,
                "LastUpdate": "2024-01-03 16:36:34",
                "Layer": null,
                "LeftCoordinate": 365,
                "MaxDateTime": null,
                "MinDateTime": null,
                "NormalizedJobStartTime": null,
                "Notes": "",
                "OwnId": "100028448903",
                "ProductName": "DATA_DEV",
                "ProjectId": "your projectId",
                "ProjectIdent": null,
                "ProjectName": null,
                "RealWorkflowId": null,
                "ResourceGroup": "your ResourceGroup",
                "RetryAble": 1,
                "RetryWait": 5,
                "RunPriority": 6,
                "ScheduleDesc": null,
                "SchedulerDesc": null,
                "SelfDepend": "serial",
                "ShowWorkflow": false,
                "SourceServiceId": ";8738;",
                "SourceServiceType": ";mysql;",
                "StartDate": null,
                "StartTime": "2024-01-03 00:00:00",
                "StartupTime": 0,
                "Status": "Y",
                "TargetServiceId": ";122116;",
                "TargetServiceType": ";hive;",
                "TaskAction": "",
                "TaskId": "your TaskId",
                "TaskLinkInfo": null,
                "TaskName": "mysql2hive_test",
                "TaskType": {
                    "TypeDesc": "离线同步",
                    "TypeId": 26,
                    "TypeSort": "数据同步"
                },
                "TaskTypeDesc": null,
                "TaskTypeId": null,
                "TenantId": "your TenantId",
                "TopCoordinate": 162,
                "TryLimit": 5,
                "UpdateTime": "2024-01-03 16:36:29",
                "UpdateUser": "hang",
                "UpdateUserId": "your UpdateUserId",
                "UserId": "your UserId",
                "VirtualFlag": false,
                "VirtualTaskId": null,
                "VirtualTaskStatus": null,
                "WorkflowId": "c66da3ee-aa0b-11ee-8d13-a4ae120f8272",
                "WorkflowName": "test11",
                "YarnQueue": null,
                "TasksStr": "your TasksStr",
                "Submit": true
            }
        ],
        "RequestId": "fe7aeb66-f05b-4241-8f8a-7d6cd6975bd6"
    }
}
```

