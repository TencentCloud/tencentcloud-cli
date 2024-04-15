**Example 1: 实例批量重跑**

实例批量重跑



Input: 

```
tccli wedata RunRerunScheduleInstances --cli-unfold-argument  \
    --Instances.0.TaskId 20240307215220701 \
    --Instances.0.CurRunDate 2024-04-10 00:00:00 \
    --Instances.0.TaskName  \
    --Instances.0.WorkflowId  \
    --Instances.0.WorkflowName  \
    --Instances.0.InCharge  \
    --Instances.0.CycleType  \
    --Instances.0.NextCurDate  \
    --Instances.0.State  \
    --Instances.0.DependenceFulfillTime  \
    --Instances.0.FirstDependenceFulfillTime  \
    --Instances.0.FirstStartTime  \
    --Instances.0.StartTime  \
    --Instances.0.EndTime  \
    --Instances.0.CostTime  \
    --Instances.0.LastLog  \
    --Instances.0.SchedulerDateTime  \
    --Instances.0.LastSchedulerDateTime  \
    --Instances.0.LastUpdate  \
    --Instances.0.CreateTime  \
    --Instances.0.DependencyRel  \
    --Instances.0.ExecutionSpace  \
    --Instances.0.FolderId  \
    --Instances.0.FolderName  \
    --Instances.0.SonList  \
    --Instances.0.ProductName  \
    --Instances.0.ResourceGroup  \
    --Instances.0.ResourceInstanceId  \
    --Instances.0.YarnQueue  \
    --Instances.0.SchedulerDesc  \
    --Instances.0.FirstSubmitTime  \
    --Instances.0.FirstRunTime  \
    --Instances.0.ProjectId 127890865433555 \
    --Instances.0.ProjectIdent  \
    --Instances.0.ProjectName  \
    --Instances.0.TenantId  \
    --Instances.0.InstanceKey  \
    --CheckFather True \
    --RerunType 2 \
    --SkipEventListening True \
    --DependentWay 1 \
    --SonInstanceType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true
        },
        "RequestId": "1d287884-1214-4b75-b4e8-383ee8e57918"
    }
}
```

