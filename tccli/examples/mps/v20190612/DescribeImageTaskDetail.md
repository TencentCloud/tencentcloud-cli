**Example 1: 获取任务详情**

查询任务结果

Input: 

```
tccli mps DescribeImageTaskDetail --cli-unfold-argument  \
    --TaskId 24000089-WorkflowTask-0723542d0c164c958ba116874fa9b0c4
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-05-16T07:44:26Z",
        "FinishTime": "2025-05-16T07:44:30Z",
        "RequestId": "147e6b46-efeb-48cf-9186-b195b2bf4f9d",
        "Status": "FINISH",
        "TaskType": "WorkflowTask"
    }
}
```

