**Example 1: 项目克隆-获取工作流任务信息**



Input: 

```
tccli wedata DescribeWorkflowTasksForProjectClone --cli-unfold-argument  \
    --ProjectId abc \
    --WorkflowId abc \
    --Page 1 \
    --Size 1 \
    --Order abc \
    --OwnerName abc \
    --StartTime abc \
    --EndTime abc \
    --FilterWorkflowName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalItems": 1,
            "TotalPages": 1,
            "CurrentPage": 1,
            "PageSize": 1,
            "CurrentPageItems": 1,
            "Items": [
                {
                    "WorkflowId": "abc",
                    "OwnerName": "abc",
                    "TaskId": "abc",
                    "TaskName": "abc",
                    "TaskType": "abc",
                    "TaskStatus": "abc",
                    "TaskLatestSubmitTime": "abc",
                    "OriginalResourceGroup": "abc",
                    "TargetResourceGroup": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

