**Example 1: 获取补录计划任务**

数据补录-获取补录计划任务

Input: 

```
tccli wedata DescribeOpsMakePlanTasks --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --ProjectId 14705274522 \
    --PlanId f47ac10b-58cc-4372-a567-0e02b2c3d479
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 0,
            "TotalPage": 0,
            "PageCount": 0,
            "PageNumber": 0,
            "PageSize": 0,
            "Items": [
                {
                    "TaskBaseInfo": {
                        "TaskId": "19920226154637701",
                        "VirtualTaskId": null,
                        "VirtualFlag": false,
                        "TaskName": "测试任务",
                        "WorkflowId": null,
                        "RealWorkflowId": null,
                        "WorkflowName": null,
                        "FolderId": null,
                        "FolderName": null,
                        "CreateTime": null,
                        "LastUpdate": null,
                        "Status": null,
                        "InCharge": "tom;jerry",
                        "InChargeId": null,
                        "StartTime": null,
                        "EndTime": null,
                        "ExecutionStartTime": null,
                        "ExecutionEndTime": null,
                        "CycleType": null,
                        "CycleStep": 1,
                        "CrontabExpression": null,
                        "DelayTime": 1,
                        "StartupTime": 1,
                        "RetryWait": 1,
                        "RetryAble": 1,
                        "TaskAction": null,
                        "TryLimit": 1,
                        "RunPriority": 1,
                        "TaskType": null,
                        "BrokerIp": null,
                        "ClusterId": null,
                        "MinDateTime": null,
                        "MaxDateTime": null,
                        "ExecutionTTL": 0,
                        "SelfDepend": null,
                        "LeftCoordinate": 0,
                        "TopCoordinate": 0,
                        "Notes": null,
                        "InstanceInitStrategy": null,
                        "YarnQueue": null,
                        "LastSchedulerCommitTime": null,
                        "NormalizedJobStartTime": null,
                        "SchedulerDesc": null,
                        "ResourceGroup": null,
                        "Creator": null,
                        "DependencyRel": null,
                        "DependencyWorkflow": null,
                        "EventListenerConfig": null,
                        "EventPublisherConfig": null,
                        "VirtualTaskStatus": null,
                        "TaskLinkInfo": {
                            "Id": null,
                            "LinkKey": null,
                            "TaskFrom": null,
                            "TaskTo": null,
                            "InCharge": null,
                            "LinkDependencyType": null,
                            "Offset": null,
                            "LinkType": null,
                            "WorkflowId": null
                        },
                        "ProductName": null,
                        "ProjectId": null,
                        "ProjectIdent": null,
                        "ProjectName": null,
                        "OwnId": null,
                        "UserId": null,
                        "TenantId": null,
                        "UpdateUser": null,
                        "UpdateTime": null,
                        "UpdateUserId": null,
                        "TaskTypeId": null,
                        "TaskTypeDesc": "Shell",
                        "ShowWorkflow": false,
                        "FirstSubmitTime": null,
                        "FirstRunTime": null,
                        "ScheduleDesc": null,
                        "CycleNum": 0,
                        "Crontab": null,
                        "StartDate": null,
                        "EndDate": null,
                        "CycleUnit": null,
                        "InitStrategy": null,
                        "Layer": null,
                        "SourceServiceId": null,
                        "SourceServiceType": null,
                        "TargetServiceId": null,
                        "TargetServiceType": null,
                        "TasksStr": null,
                        "Submit": true,
                        "ExecutorGroupId": null,
                        "ExecutorGroupName": null
                    },
                    "InstanceCount": 0,
                    "CompletePercent": 0,
                    "SuccessPercent": 0,
                    "InstanceTotalCount": 0
                }
            ]
        },
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

