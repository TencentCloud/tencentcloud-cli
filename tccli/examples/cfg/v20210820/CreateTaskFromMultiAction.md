**Example 1: 示例**



Input: 

```
tccli cfg CreateTaskFromMultiAction --cli-unfold-argument  \
    --TaskInstances ins-xxxxxxxx \
    --TaskTitle title \
    --TaskDescription desc \
    --TaskPauseDuration 1 \
    --TaskAction.0.TaskActionId 0 \
    --TaskAction.0.TaskActionGeneralConfiguration {"duration": 0} \
    --TaskAction.0.TaskActionCustomConfiguration {"timeout": 0}
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

