**Example 1: 查询新增的forcemerge任务列表**

查询新增的forcemerge任务列表

Input: 

```
tccli es DescribeForceMergeTask --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "50df75f7-ec95-4c32-b7b0-a8e98ae74fef11",
        "CrontabTaskInfo": [
            {
                "TaskId": 2000,
                "RegionId": 1,
                "InstanceId": 14268,
                "TaskName": "自定义的任务名称",
                "TaskType": "ForceMerge",
                "TaskTime": "21:00",
                "Target": ".kibana",
                "LastExecTime": "",
                "State": "enable",
                "TaskDetail": "******",
                "TaskStatus": 0,
                "CreateTime": "2023-06-19 20:27:33",
                "UpdateTime": "2023-06-19 20:27:33"
            },
            {
                "TaskId": 2002,
                "RegionId": 1,
                "InstanceId": 14268,
                "TaskName": "自定义的任务名称",
                "TaskType": "ForceMerge",
                "TaskTime": "22:00",
                "Target": ".kibana",
                "LastExecTime": "",
                "State": "enable",
                "TaskDetail": "******",
                "TaskStatus": 0,
                "CreateTime": "2023-06-19 20:27:33",
                "UpdateTime": "2023-06-19 20:27:33"
            }
        ]
    }
}
```

