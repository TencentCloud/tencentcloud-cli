**Example 1: 分页查询任务运行历史**

分页查询任务运行历史

Input: 

```
tccli wedata DescribeTaskRunHistory --cli-unfold-argument  \
    --ProjectId abc \
    --SearchCondition.CycleList abc \
    --SearchCondition.DateFrom abc \
    --SearchCondition.DateTo abc \
    --SearchCondition.Instance.ExecutionSpace abc \
    --SearchCondition.Instance.ProductName abc \
    --SearchCondition.Keyword abc \
    --SearchCondition.Sort abc \
    --SearchCondition.SortCol abc \
    --SearchCondition.StateList abc \
    --PageSize 1 \
    --PageNumber abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
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
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

