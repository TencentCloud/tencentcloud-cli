**Example 1: 【克隆任务模式】获取任务列表**



Input: 

```
tccli wedata DescribeTasksForProjectClone --cli-unfold-argument  \
    --ProjectId abc \
    --Page 1 \
    --Size 1 \
    --Order abc \
    --FilterTaskName abc \
    --OwnerName abc \
    --WorkflowName abc \
    --TaskStatus abc \
    --StartTime abc \
    --EndTime abc
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
                    "WorkflowName": "abc",
                    "OwnerName": "abc",
                    "TaskId": "abc",
                    "TaskName": "abc",
                    "TaskType": "abc",
                    "TaskStatus": "abc",
                    "TaskLatestSubmitTime": "abc",
                    "FolderName": "abc",
                    "VirtualFlag": true
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误用例**

错误用例

Input: 

```
tccli wedata DescribeTasksForProjectClone --cli-unfold-argument  \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "43990a89-081f-45b4-a6af-06c8f5d08409"
    }
}
```

