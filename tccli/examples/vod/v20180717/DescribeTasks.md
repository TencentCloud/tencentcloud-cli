**Example 1: 获取任务列表**

获取任务列表

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
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx123"
            },
            {
                "TaskId": "taskId2",
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx124"
            },
            {
                "TaskId": "taskId3",
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx125"
            },
            {
                "TaskId": "taskId4",
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx126"
            },
            {
                "TaskId": "taskId5",
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx127"
            }
        ],
        "ScrollToken": "taskId6",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 2: 获取任务列表-翻页**

获取任务列表-翻页

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
                "Status": "FINISH",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx124"
            }
        ],
        "ScrollToken": "abc",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 3: 获取任务列表-处理中**

获取任务列表-处理中

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
                "Status": "PROCESSING",
                "TaskType": "transcode",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "0001-01-01T00:00:00Z",
                "SessionContext": "",
                "SessionId": "",
                "FileId": "528xx124"
            }
        ],
        "ScrollToken": "abc",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

