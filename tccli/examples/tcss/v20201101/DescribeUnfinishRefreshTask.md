**Example 1: 查询是否存在未完成刷新任务示例**



Input: 

```
tccli tcss DescribeUnfinishRefreshTask --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskId": 1,
        "TaskStatus": "AssetCheckFinished",
        "NewTaskID": "1700157600010579384",
        "RequestId": "f249013b-c9ca-444c-8430-2f97a422859a"
    }
}
```

