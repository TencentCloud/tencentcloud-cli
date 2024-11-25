**Example 1: 示例**



Input: 

```
tccli cfg CreateTaskFromMultiAction --cli-unfold-argument  \
    --TaskInstances abc \
    --TaskTitle abc \
    --TaskDescription abc \
    --TaskPauseDuration 1 \
    --TaskAction.0.TaskActionId 0 \
    --TaskAction.0.TaskActionGeneralConfiguration abc \
    --TaskAction.0.TaskActionCustomConfiguration abc
```

Output: 
```
{
    "Response": {
        "RequestId": "f0aee8ac-2ed3-4a7f-a25b-f0d7d228dd30",
        "TaskId": 50
    }
}
```

