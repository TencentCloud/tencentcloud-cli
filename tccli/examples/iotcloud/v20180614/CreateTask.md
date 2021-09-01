**Example 1: 创建任务**



Input: 

```
tccli iotcloud CreateTask --cli-unfold-argument  \
    --TaskType UpdateShadow \
    --ProductId ABCDE12345 \
    --DeviceNameFilter  \
    --ScheduleTimeInSeconds 0 \
    --MaxExecutionTimeInSeconds  \
    --Tasks.UpdateShadowTask.Desired {\"color\":\"red\"}
```

Output: 
```
{
    "Response": {
        "TaskId": "dsaudhuisadhada",
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

