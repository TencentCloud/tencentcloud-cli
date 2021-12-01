**Example 1: 任务执行中**



Input: 

```
tccli ivld DescribeTask --cli-unfold-argument  \
    --TaskId task-g8lqk734
```

Output: 
```
{
    "Response": {
        "RequestId": "a3010447-5003-4358-9b85-7c81a98b1c8d",
        "TaskInfo": {
            "FailedReason": "",
            "MediaId": "media-a1b2c3d4",
            "MediaPreknownInfo": {
                "MediaLabel": 1,
                "MediaLang": 1,
                "MediaSecondLabel": 0,
                "MediaType": 2
            },
            "TaskCreateTime": 1634092320,
            "TaskId": "task-g8lqk734",
            "TaskName": "demo-task-0",
            "TaskProgress": 2,
            "TaskStartTime": 1634092324,
            "TaskStatus": 2,
            "TaskTimeCost": 0
        }
    }
}
```

**Example 2: 任务执行完成**



Input: 

```
tccli ivld DescribeTask --cli-unfold-argument  \
    --TaskId task-g8lqk734
```

Output: 
```
{
    "Response": {
        "RequestId": "af5fa625-286e-431d-b52c-6c577048e987",
        "TaskInfo": {
            "FailedReason": "",
            "MediaId": "media-a1b2c3d4",
            "MediaPreknownInfo": {
                "MediaLabel": 1,
                "MediaLang": 1,
                "MediaSecondLabel": 0,
                "MediaType": 2
            },
            "TaskCreateTime": 1634092320,
            "TaskId": "task-g8lqk734",
            "TaskName": "demo-task-0",
            "TaskProgress": 0,
            "TaskStartTime": 1634092324,
            "TaskStatus": 8,
            "TaskTimeCost": 114
        }
    }
}
```

