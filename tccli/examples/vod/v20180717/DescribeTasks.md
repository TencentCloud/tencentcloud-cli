**Example 1: Getting task list**



Input: 

```
tccli vod DescribeTasks --cli-unfold-argument  \
    --Status FINISH \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "taskId1",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId2",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId3",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId4",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId5",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            }
        ],
        "ScrollToken": "taskId6",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 2: Getting task list - processing**



Input: 

```
tccli vod DescribeTasks --cli-unfold-argument  \
    --Status PROCESSING \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "taskId7",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": null
            }
        ],
        "ScrollToken": null,
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 3: Getting task list - scrolling**



Input: 

```
tccli vod DescribeTasks --cli-unfold-argument  \
    --Status FINISH \
    --Limit 5 \
    --ScrollToken taskId6
```

Output: 
```
{
    "Response": {
        "TaskSet": [
            {
                "TaskId": "taskId6",
                "Type": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            }
        ],
        "ScrollToken": null,
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

