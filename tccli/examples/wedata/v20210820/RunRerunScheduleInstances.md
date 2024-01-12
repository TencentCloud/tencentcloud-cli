**Example 1: 1**

1

Input: 

```
tccli wedata RunRerunScheduleInstances --cli-unfold-argument  \
    --Instances.0.TaskId  \
    --Instances.0.TaskName  \
    --Instances.0.WorkflowId  \
    --Instances.0.WorkflowName  \
    --Instances.0.InCharge  \
    --Instances.0.CycleType  \
    --Instances.0.CurRunDate  \
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
    --Instances.0.ProjectId  \
    --Instances.0.ProjectIdent  \
    --Instances.0.ProjectName  \
    --Instances.0.TenantId  \
    --Instances.0.InstanceKey  \
    --RerunType  \
    --DependentWay  \
    --SonInstanceType 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "JSON parse error: Cannot deserialize value of type `com.tencent.tbds.guldan.api.store.service.api.utils.TaskCycleType` from String \"\": not one of the values accepted for Enum class: [ONEOFF_CYCLE, ELASTICITY_WEEK_CYCLE, DAY_CYCLE, YEAR_CYCLE, USER_DRIVE, MONTH_CYCLE, ELASTICITY_YUE_CYCLE, HOUR_CYCLE, CRONTAB_CYCLE, INSTANT, WEEK_CYCLE, MINUTE_CYCLE]; nested exception is com.fasterxml.jackson.databind.exc.InvalidFormatException: Cannot deserialize value of type `com.tencent.tbds.guldan.api.store.service.api.utils.TaskCycleType` from String \"\": not one of the values accepted for Enum class: [ONEOFF_CYCLE, ELASTICITY_WEEK_CYCLE, DAY_CYCLE, YEAR_CYCLE, USER_DRIVE, MONTH_CYCLE, ELASTICITY_YUE_CYCLE, HOUR_CYCLE, CRONTAB_CYCLE, INSTANT, WEEK_CYCLE, MINUTE_CYCLE]\n at [Source: (PushbackInputStream); line: 1, column: 102] (through reference chain: com.tencent.wedata.ai.ops.api.web.request.InstanceOpsRequest[\"Instances\"]->java.util.ArrayList[0]->com.tencent.wedata.ai.ops.commons.dto.scheduler.InstanceOpsDto[\"CycleType\"])"
        },
        "RequestId": "6896b274-816f-4523-a417-5555464a9e18"
    }
}
```

