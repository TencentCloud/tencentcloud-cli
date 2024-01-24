**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeWorkflowSchedulerInfoDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId f5d1b42f-ed67-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": null,
            "Creater": null,
            "CrontabExpression": null,
            "CycleStep": 1,
            "CycleType": "DAY_CYCLE",
            "DelayTime": 0,
            "DependencyWorkflow": "no",
            "EndTime": "2099-12-31 23:59:59",
            "ExecutionEndTime": null,
            "ExecutionStartTime": null,
            "FirstSubmitTime": null,
            "InstanceInitStrategy": "T_PLUS_0",
            "LatestSubmitTime": null,
            "ModifyTime": null,
            "ProjectId": "1460947878944567296",
            "SchedulerDesc": "每天00:00执行一次",
            "SelfDepend": "serial",
            "StartTime": "2023-05-12 12:04:17",
            "StartupTime": 0,
            "TaskAction": "",
            "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
        },
        "RequestId": "4d12dcf0-83ef-40b9-a254-98bd6e168991"
    }
}
```

