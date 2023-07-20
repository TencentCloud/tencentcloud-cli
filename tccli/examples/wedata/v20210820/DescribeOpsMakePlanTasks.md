**Example 1: 成功获取补录计划任务**

成功获取补录计划任务

Input: 

```
tccli wedata DescribeOpsMakePlanTasks --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId 147056160274522xxxx \
    --PlanId e0bed861-0e95-44ca-9d10-28f29752xxxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CompletePercent": 100,
                    "InstanceCount": 12,
                    "SuccessPercent": 100,
                    "TaskBaseInfo": {
                        "BrokerIp": null,
                        "ClusterId": null,
                        "CreateTime": null,
                        "Creator": null,
                        "Crontab": null,
                        "CrontabExpression": null,
                        "CycleNum": null,
                        "CycleStep": null,
                        "CycleType": null,
                        "CycleUnit": null,
                        "DelayTime": null,
                        "DependencyRel": null,
                        "DependencyWorkflow": null,
                        "EndDate": null,
                        "EndTime": null,
                        "EventListenerConfig": null,
                        "EventPublisherConfig": null,
                        "ExecutionEndTime": null,
                        "ExecutionStartTime": null,
                        "ExecutionTTL": null,
                        "FirstRunTime": null,
                        "FirstSubmitTime": null,
                        "FolderId": null,
                        "FolderName": null,
                        "InCharge": "incharge_xxx",
                        "InChargeId": null,
                        "InitStrategy": null,
                        "InstanceInitStrategy": null,
                        "LastSchedulerCommitTime": null,
                        "LastUpdate": null,
                        "Layer": null,
                        "LeftCoordinate": null,
                        "MaxDateTime": null,
                        "MinDateTime": null,
                        "NormalizedJobStartTime": null,
                        "Notes": null,
                        "OwnId": null,
                        "ProductName": null,
                        "ProjectId": null,
                        "ProjectIdent": null,
                        "ProjectName": null,
                        "RealWorkflowId": null,
                        "ResourceGroup": null,
                        "RetryAble": null,
                        "RetryWait": null,
                        "RunPriority": null,
                        "ScheduleDesc": null,
                        "SchedulerDesc": null,
                        "SelfDepend": null,
                        "ShowWorkflow": false,
                        "SourceServiceId": null,
                        "SourceServiceType": null,
                        "StartDate": null,
                        "StartTime": null,
                        "StartupTime": null,
                        "Status": null,
                        "TargetServiceId": null,
                        "TargetServiceType": null,
                        "TaskAction": null,
                        "TaskId": "2023052809431xxxx",
                        "TaskLinkInfo": null,
                        "TaskName": "部分成功任务子任务",
                        "TaskType": null,
                        "TaskTypeDesc": "Shell",
                        "TaskTypeId": null,
                        "TenantId": null,
                        "TopCoordinate": null,
                        "TryLimit": null,
                        "UpdateTime": null,
                        "UpdateUser": null,
                        "UpdateUserId": null,
                        "UserId": null,
                        "VirtualFlag": false,
                        "VirtualTaskId": null,
                        "VirtualTaskStatus": null,
                        "WorkflowId": null,
                        "WorkflowName": null,
                        "YarnQueue": null
                    }
                }
            ],
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1,
            "TotalPage": 1
        },
        "RequestId": "36f271a5-97ab-47fc-865b-5c3eaf2axxxx"
    }
}
```

