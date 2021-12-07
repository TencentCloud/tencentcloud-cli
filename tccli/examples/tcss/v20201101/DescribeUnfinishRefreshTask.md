**Example 1: 查询是否存在未完成刷新任务示例**



Input: 

```
tccli tcss DescribeUnfinishRefreshTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e7e5ce68-b074-4fb7-8354-f2b87260063e",
        "TaskId": 0,
        "TaskStatus": "Task_NoExist"
    }
}
```

