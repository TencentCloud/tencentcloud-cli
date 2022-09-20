**Example 1: 获取任务列表**



Input: 

```
tccli mps DescribeTasks --cli-unfold-argument  \
    --Status FINISH \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 12,
        "TaskSet": [
            {
                "TaskId": "taskId1",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId2",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId3",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId4",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            },
            {
                "TaskId": "taskId5",
                "TaskType": "WorkflowTask",
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

**Example 2: 获取任务列表-处理中**



Input: 

```
tccli mps DescribeTasks --cli-unfold-argument  \
    --Status PROCESSING \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskSet": [
            {
                "TaskId": "taskId7",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "0000-00-00T00:00:00Z"
            }
        ],
        "ScrollToken": "",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 3: 获取任务列表-翻页**



Input: 

```
tccli mps DescribeTasks --cli-unfold-argument  \
    --Status FINISH \
    --ScrollToken taskId6 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TaskSet": [
            {
                "TaskId": "taskId6",
                "TaskType": "WorkflowTask",
                "CreateTime": "2018-12-27T13:57:15Z",
                "BeginProcessTime": "2018-12-27T13:57:15Z",
                "FinishTime": "2018-12-27T13:57:15Z"
            }
        ],
        "ScrollToken": "",
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

