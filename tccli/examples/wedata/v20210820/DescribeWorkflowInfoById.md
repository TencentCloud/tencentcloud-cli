**Example 1: 通过工作流id，查询工作流详情**

通过工作流id，查询工作流详情

Input: 

```
tccli wedata DescribeWorkflowInfoById --cli-unfold-argument  \
    --WorkflowId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "abc",
            "Creator": "abc",
            "ModifyTime": "abc",
            "DelayTime": 1,
            "StartupTime": 1,
            "SelfDepend": "abc",
            "StartTime": "abc",
            "EndTime": "abc",
            "TaskAction": "abc",
            "CycleType": "abc",
            "CycleStep": 1,
            "CrontabExpression": "abc",
            "ExecutionStartTime": "abc",
            "ExecutionEndTime": "abc",
            "InstanceInitStrategy": "abc",
            "WorkflowId": "abc",
            "DependencyWorkflow": "abc",
            "SchedulerDesc": "abc",
            "FirstSubmitTime": "abc",
            "LatestSubmitTime": "abc"
        },
        "RequestId": "abc"
    }
}
```

