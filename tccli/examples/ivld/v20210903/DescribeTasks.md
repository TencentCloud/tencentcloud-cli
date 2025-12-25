**Example 1: 描述前5个完成的任务**



Input: 

```
tccli ivld DescribeTasks --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 5 \
    --TaskFilter.TaskStatusSet 8
```

Output: 
```
{
    "Response": {
        "RequestId": "dcbd578a-caea-487a-b761-d49c9b7f2ac3",
        "TaskInfoSet": [
            {
                "AudioMetadata": null,
                "CallbackURL": "",
                "FailedReason": "",
                "ImageMetadata": null,
                "Label": "",
                "MediaId": "media-fdk9hp2v",
                "MediaName": "",
                "MediaPreknownInfo": {
                    "MediaLabel": 1,
                    "MediaLang": 1,
                    "MediaSecondLabel": 1,
                    "MediaType": 2
                },
                "Metadata": null,
                "TaskCreateTime": "2025-12-23T16:51:03+08:00",
                "TaskId": "task-ctl3bk8k",
                "TaskName": "TaskNameTest",
                "TaskProgress": 0,
                "TaskStartTime": "2025-12-23T16:52:54+08:00",
                "TaskStatus": 8,
                "TaskTimeCost": 111,
                "TextMetadata": null
            },
            {
                "AudioMetadata": null,
                "CallbackURL": "",
                "FailedReason": "",
                "ImageMetadata": null,
                "Label": "",
                "MediaId": "media-t9Igr9jf",
                "MediaName": "",
                "MediaPreknownInfo": {
                    "MediaLabel": 1,
                    "MediaLang": 1,
                    "MediaSecondLabel": 0,
                    "MediaType": 2
                },
                "Metadata": null,
                "TaskCreateTime": "2025-12-23T16:51:03+08:00",
                "TaskId": "task-wodahg5t",
                "TaskName": "test-task-0",
                "TaskProgress": 0,
                "TaskStartTime": "2025-12-23T16:51:04+08:00",
                "TaskStatus": 8,
                "TaskTimeCost": 131,
                "TextMetadata": null
            },
            {
                "AudioMetadata": null,
                "CallbackURL": "",
                "FailedReason": "",
                "ImageMetadata": null,
                "Label": "",
                "MediaId": "media-fdk9hp2u",
                "MediaName": "",
                "MediaPreknownInfo": {
                    "MediaLabel": 1,
                    "MediaLang": 1,
                    "MediaSecondLabel": 1,
                    "MediaType": 2
                },
                "Metadata": null,
                "TaskCreateTime": "2025-12-23T16:51:03+08:00",
                "TaskId": "task-qq38azcb",
                "TaskName": "TaskNameTest",
                "TaskProgress": 0,
                "TaskStartTime": "2025-12-23T16:51:05+08:00",
                "TaskStatus": 8,
                "TaskTimeCost": 138,
                "TextMetadata": null
            },
            {
                "AudioMetadata": null,
                "CallbackURL": "",
                "FailedReason": "",
                "ImageMetadata": null,
                "Label": "",
                "MediaId": "media-fdk9hp2u",
                "MediaName": "",
                "MediaPreknownInfo": {
                    "MediaLabel": 1,
                    "MediaLang": 1,
                    "MediaSecondLabel": 1,
                    "MediaType": 2
                },
                "Metadata": null,
                "TaskCreateTime": "2025-12-23T14:51:01+08:00",
                "TaskId": "task-kzjesg12",
                "TaskName": "TaskNameTest",
                "TaskProgress": 0,
                "TaskStartTime": "2025-12-23T14:52:54+08:00",
                "TaskStatus": 8,
                "TaskTimeCost": 148,
                "TextMetadata": null
            },
            {
                "AudioMetadata": null,
                "CallbackURL": "",
                "FailedReason": "",
                "ImageMetadata": null,
                "Label": "",
                "MediaId": "media-ly5qgk6j",
                "MediaName": "",
                "MediaPreknownInfo": {
                    "MediaLabel": 1,
                    "MediaLang": 1,
                    "MediaSecondLabel": 1,
                    "MediaType": 2
                },
                "Metadata": null,
                "TaskCreateTime": "2025-12-23T12:50:48+08:00",
                "TaskId": "task-krmtkhia",
                "TaskName": "demo-task-0",
                "TaskProgress": 0,
                "TaskStartTime": "2025-12-23T12:52:50+08:00",
                "TaskStatus": 8,
                "TaskTimeCost": 111,
                "TextMetadata": null
            }
        ],
        "TotalCount": 17
    }
}
```

