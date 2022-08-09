**Example 1: 范例**



Input: 

```
tccli wedata ModifyWorkflowSchedule --cli-unfold-argument  \
    --WorkflowId 34e51bc4-0cd9-11ed-8909-bc97e105ba60 \
    --StartupTime 47483648 \
    --SelfDepend 1 \
    --ProjectId 1 \
    --ExecutionEndTime  \
    --TaskAction  \
    --DelayTime 1 \
    --DependencyWorkflow no \
    --StartTime 2022-03-03 11:12:59 \
    --ExecutionStartTime  \
    --EndTime 2022-09-03 11:12:59 \
    --CycleType 1 \
    --CycleStep 3 \
    --CrontabExpression 
```

Output: 
```
{
    "Response": {
        "RequestId": "dc5397bb-aa83-4ae2-8950-74e6f734102c",
        "Data": {
            "Running": 0,
            "Success": 0,
            "Failed": 0,
            "Total": 0
        }
    }
}
```

**Example 2: 范例2**



Input: 

```
tccli wedata ModifyWorkflowSchedule --cli-unfold-argument  \
    --WorkflowId 34e51bc4-0cd9-11ed-8909-bc97e105ba60 \
    --StartupTime 47483648 \
    --SelfDepend 1 \
    --ProjectId 1 \
    --ExecutionEndTime  \
    --TaskAction  \
    --DelayTime 1 \
    --DependencyWorkflow no \
    --StartTime 2022-03-03 11:12:59 \
    --ExecutionStartTime  \
    --EndTime 2022-09-03 11:12:59 \
    --CycleType 1 \
    --CycleStep 3 \
    --CrontabExpression 
```

Output: 
```
{
    "Response": {
        "RequestId": "c20f7fea-d73f-44cd-94a5-1d9f884df5cf",
        "Data": {
            "Running": 0,
            "Success": 0,
            "Failed": 0,
            "Total": 0
        }
    }
}
```

