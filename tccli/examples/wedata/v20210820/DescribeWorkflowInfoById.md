**Example 1: 工作流详情demo**

工作流详情demo

Input: 

```
tccli wedata DescribeWorkflowInfoById --cli-unfold-argument  \
    --WorkflowId 3db9f4ad-e0e2-11ee-8ec8-b8599f277de5 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": null,
            "Creator": null,
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
            "SchedulerDesc": "每天00:00执行一次",
            "SelfDepend": "serial",
            "StartTime": "2024-04-10 16:31:55",
            "StartupTime": 0,
            "TaskAction": "",
            "WorkflowId": "3db9f4ad-e0e2-11ee-8ec8-b8599f277de5"
        },
        "RequestId": "b91acd1a-1ca9-4d94-9647-e032924ac6bc"
    }
}
```

