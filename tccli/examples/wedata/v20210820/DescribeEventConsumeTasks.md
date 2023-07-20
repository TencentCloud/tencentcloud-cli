**Example 1: 成功获取事件实例消费任务**

成功获取事件实例消费任务

Input: 

```
tccli wedata DescribeEventConsumeTasks --cli-unfold-argument  \
    --EventCaseId 9e2a0e1f870ec340018712b3925f0006 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ConsumeLogId": "9eb04578870ec50d018712b3938d0005",
                    "ConsumerDetail": {
                        "BrokerIp": "any",
                        "ClusterId": null,
                        "CreateTime": "2023-03-24 16:09:14",
                        "Creator": "stackxchen",
                        "Crontab": null,
                        "CrontabExpression": null,
                        "CycleNum": null,
                        "CycleStep": 5,
                        "CycleType": "MINUTE_CYCLE",
                        "CycleUnit": null,
                        "DelayTime": 0,
                        "DependencyRel": "and",
                        "DependencyWorkflow": "no",
                        "EndDate": null,
                        "EndTime": "2023-03-24 23:59:59",
                        "EventListenerConfig": null,
                        "EventPublisherConfig": null,
                        "ExecutionEndTime": null,
                        "ExecutionStartTime": null,
                        "ExecutionTTL": -1,
                        "FirstRunTime": null,
                        "FirstSubmitTime": null,
                        "FolderId": null,
                        "FolderName": null,
                        "InCharge": "stackxchen",
                        "InChargeId": "100028590605",
                        "InitStrategy": null,
                        "InstanceInitStrategy": "T_PLUS_0",
                        "LastSchedulerCommitTime": null,
                        "LastUpdate": "2023-03-24 16:18:31",
                        "Layer": null,
                        "LeftCoordinate": 376,
                        "MaxDateTime": null,
                        "MinDateTime": null,
                        "NormalizedJobStartTime": null,
                        "Notes": "",
                        "OwnId": "100028448903",
                        "ProductName": "DATA_DEV",
                        "ProjectId": "1460963739345731584",
                        "ProjectIdent": "us_pre",
                        "ProjectName": "调度预发验证项目",
                        "RealWorkflowId": null,
                        "ResourceGroup": "20221221143954438902",
                        "RetryAble": 1,
                        "RetryWait": 5,
                        "RunPriority": 6,
                        "ScheduleDesc": null,
                        "SchedulerDesc": "从2023年03月24日 00:00:00开始，每间隔5分钟执行一次",
                        "SelfDepend": "parallel",
                        "ShowWorkflow": false,
                        "SourceServiceId": null,
                        "SourceServiceType": null,
                        "StartDate": null,
                        "StartTime": "2023-03-24 00:00:00",
                        "StartupTime": 0,
                        "Status": "Y",
                        "TargetServiceId": null,
                        "TargetServiceType": null,
                        "TaskAction": "",
                        "TaskId": "20230324160914089",
                        "TaskLinkInfo": null,
                        "TaskName": "test_event_minute",
                        "TaskType": {
                            "TypeDesc": "Shell",
                            "TypeId": 35,
                            "TypeSort": "数据计算"
                        },
                        "TaskTypeDesc": null,
                        "TaskTypeId": null,
                        "TenantId": "1315051789",
                        "TopCoordinate": 247,
                        "TryLimit": 5,
                        "UpdateTime": "2023-03-24 16:18:29",
                        "UpdateUser": "stackxchen",
                        "UpdateUserId": "100028590605",
                        "UserId": "100028590605",
                        "VirtualFlag": false,
                        "VirtualTaskId": null,
                        "VirtualTaskStatus": null,
                        "WorkflowId": "68ce6df0-7b80-11ed-a3a7-b8cef6c14251",
                        "WorkflowName": "dev_test",
                        "YarnQueue": null
                    },
                    "ConsumerId": "20230324160914089",
                    "CreationTimestamp": "2023-03-24T08:19:31.340Z",
                    "EventCaseId": "9e2a0e1f870ec340018712b3925f0006"
                }
            ],
            "PageCount": 1,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "b7d1e5cf-3454-48db-a261-41a760f70ee6"
    }
}
```

