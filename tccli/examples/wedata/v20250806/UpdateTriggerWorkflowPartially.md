**Example 1: 更新工作流成功**

更新工作流成功

Input: 

```
tccli wedata UpdateTriggerWorkflowPartially --cli-unfold-argument  \
    --ProjectId 3310733480531783680 \
    --WorkflowId 2248eb04-d812-4041-b3cb-2d20a602fc79 \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.ExtraInfo  \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.ConfigMode COMMON \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.TriggerId 33153442-9785-11f1-b20e-b8599fc0ab4a \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.FileArrivalPath cosn://dqtest8-251433363/ \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.TriggerMinimumInterval 5 \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.TriggerWaitTime 5 \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.FileNamePattern t1.csv \
    --NewSetting.TriggerWorkflowSchedulerConfigurations.0.Recursive 1 \
    --NewSetting.TriggerWorkflowRunConfiguration.MaxConcurrentNum 1 \
    --NewSetting.TriggerWorkflowRunConfiguration.QueuingMode 1 \
    --NewSetting.SchedulerStatus PAUSED \
    --NewSetting.TriggerMode FILE_ARRIVAL
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "bad98336-674c-4eaa-8224-5ede55488f7c"
    }
}
```

