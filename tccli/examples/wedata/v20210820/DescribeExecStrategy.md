**Example 1: 例子**



Input: 

```
tccli wedata DescribeExecStrategy --cli-unfold-argument  \
    --RuleGroupId 1 \
    --ProjectId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "b6347c5c-10bd-4c70-b066-bc62ccbff7be",
        "Data": {
            "RuleGroupId": null,
            "MonitorType": 2,
            "ExecQueue": "root.default",
            "ExecutorGroupId": "1",
            "ExecutorGroupName": "worker",
            "Tasks": [
                {
                    "TaskId": "1",
                    "TaskName": "task_1",
                    "WorkflowId": "1"
                }
            ],
            "StartTime": null,
            "EndTime": null,
            "CycleType": "H",
            "CycleStep": 1,
            "TaskAction": "1",
            "DelayTime": 1
        }
    }
}
```

