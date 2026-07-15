**Example 1: 获取图片处理任务列表**

获取图片处理任务列表

Input: 

```
tccli mps DescribeImageTasks --cli-unfold-argument  \
    --Status FINISH \
    --Limit 20 \
    --SubTaskHasFailed False \
    --ScrollToken ********-WorkflowTask-********************************tt6
```

Output: 
```
{
    "Response": {
        "ScrollToken": "********-WorkflowTask-********************************tt6",
        "TaskSet": [
            {
                "BeginProcessTime": "2026-03-16T12:29:54Z",
                "CreateTime": "2026-03-16T12:29:54Z",
                "FinishTime": "2026-03-16T12:29:56Z",
                "Status": "FINISH",
                "SubTaskHasFailed": false,
                "TaskId": "********-WorkflowTask-********************************tt6"
            }
        ],
        "TotalCount": 13,
        "RequestId": "f642575f-60b2-46ef-a1c1-5401b6e9ba33"
    }
}
```

