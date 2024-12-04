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
            "MediaName": "本地新闻",
            "Label": "",
            "CallbackURL": "http://example.com/api/callback",
            "FailedReason": "",
            "MediaId": "media-2aHsU6sj",
            "MediaPreknownInfo": {
                "MediaLabel": 1,
                "MediaLang": 1,
                "MediaSecondLabel": 0,
                "MediaType": 2
            },
            "TaskCreateTime": "2006-01-02T15:04:05Z07:00",
            "TaskId": "task-g8lqk734",
            "TaskName": "demo-task-0",
            "TaskProgress": 2,
            "TaskStartTime": "2006-01-02T15:04:05Z07:00",
            "TaskStatus": 2,
            "TaskTimeCost": 0,
            "AudioMetadata": null,
            "ImageMetadata": null,
            "TextMetadata": null,
            "Metadata": null
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
            "MediaName": "本地新闻",
            "Label": "",
            "CallbackURL": "http://example.com/api/callback",
            "FailedReason": "",
            "MediaId": "media-2aHsU6sj",
            "MediaPreknownInfo": {
                "MediaLabel": 1,
                "MediaLang": 1,
                "MediaSecondLabel": 0,
                "MediaType": 2
            },
            "TaskCreateTime": "2006-01-02T15:04:05Z07:00",
            "TaskId": "task-g8lqk734",
            "TaskName": "demo-task-0",
            "TaskProgress": 0,
            "TaskStartTime": "2006-01-02T15:04:05Z07:00",
            "TaskStatus": 8,
            "TaskTimeCost": 114,
            "AudioMetadata": null,
            "ImageMetadata": null,
            "TextMetadata": null,
            "Metadata": null
        }
    }
}
```

