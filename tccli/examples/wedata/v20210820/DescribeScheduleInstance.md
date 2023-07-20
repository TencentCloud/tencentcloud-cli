**Example 1: 查询任务实例**

查询任务实例

Input: 

```
tccli wedata DescribeScheduleInstance --cli-unfold-argument  \
    --TaskId abc \
    --CurRunDate 2022-01-01 00:00:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "abc",
            "TaskName": "abc",
            "WorkflowId": "abc",
            "WorkflowName": "abc",
            "InCharge": "abc",
            "CycleType": "abc",
            "CurRunDate": "abc",
            "NextCurDate": "abc",
            "RunPriority": 1,
            "TryLimit": 1,
            "Tries": 1,
            "TotalRunNum": 1,
            "DoFlag": 1,
            "RedoFlag": 1,
            "State": "abc",
            "RuntimeBroker": "abc",
            "ErrorDesc": "abc",
            "TaskType": {
                "TypeDesc": "abc",
                "TypeId": 0,
                "TypeSort": "abc"
            },
            "DependenceFulfillTime": "abc",
            "FirstDependenceFulfillTime": "abc",
            "FirstStartTime": "abc",
            "StartTime": "abc",
            "EndTime": "abc",
            "CostTime": "abc",
            "CostMillisecond": 1,
            "MaxCostTime": 1,
            "MinCostTime": 1,
            "AvgCostTime": 0,
            "LastLog": "abc",
            "SchedulerDateTime": "abc",
            "LastSchedulerDateTime": "abc",
            "LastUpdate": "abc",
            "CreateTime": "abc",
            "DependencyRel": "abc",
            "ExecutionSpace": "abc",
            "IgnoreEvent": true,
            "VirtualFlag": true,
            "FolderId": "abc",
            "FolderName": "abc",
            "SonList": "abc",
            "ProductName": "abc",
            "ResourceGroup": "abc",
            "ResourceInstanceId": "abc",
            "YarnQueue": "abc",
            "SchedulerDesc": "abc",
            "FirstSubmitTime": "abc",
            "FirstRunTime": "abc",
            "ProjectId": "abc",
            "ProjectIdent": "abc",
            "ProjectName": "abc",
            "TenantId": "abc"
        },
        "RequestId": "abc"
    }
}
```

