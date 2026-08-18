**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata UpdateTriggerWorkflow --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId c6df7416-ee03-405e-adf1-094d26b8c98b \
    --WorkflowName test_wk_2
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "e213b6b0-385b-482d-ae96-3f1d0e81d944"
    }
}
```

**Example 2: 成功示例2**

成功示例2

Input: 

```
tccli wedata UpdateTriggerWorkflow --cli-unfold-argument  \
    --ProjectId 31*6203***********0 \
    --WorkflowId 90d110b4-79b4-4617-87f4-eee91a821fad \
    --WorkflowName ******_workflow_0729 \
    --OwnerUin *0****8936*1 \
    --WorkflowDesc 1 \
    --TriggerWorkflowSchedulerConfigurations.0.TriggerMode TIME_TRIGGER \
    --TriggerWorkflowSchedulerConfigurations.0.ScheduleTimeZone UTC+8 \
    --TriggerWorkflowSchedulerConfigurations.0.StartTime 2026-07-29 00:00:00 \
    --TriggerWorkflowSchedulerConfigurations.0.EndTime 2099-12-31 23:59:59 \
    --TriggerWorkflowSchedulerConfigurations.0.ConfigMode COMMON \
    --TriggerWorkflowSchedulerConfigurations.0.CycleType DAY_CYCLE \
    --TriggerWorkflowSchedulerConfigurations.0.CrontabExpression 0 0 0 * * ? * \
    --TriggerWorkflowSchedulerConfigurations.0.TriggerId af1f5d11-8b49-11f1-9a90-0c42a11d9e4a \
    --TriggerWorkflowSchedulerConfigurations.0.SchedulerStatus ACTIVE \
    --TriggerWorkflowRunConfiguration.MaxConcurrentNum 1 \
    --TriggerWorkflowRunConfiguration.QueuingMode 1 \
    --SchedulerStatus ACTIVE \
    --TriggerMode TIME_TRIGGER \
    --ExecuteUserUin ****01******
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "dd582699-b79b-4fc7-a9aa-2b47e961dda0"
    }
}
```

