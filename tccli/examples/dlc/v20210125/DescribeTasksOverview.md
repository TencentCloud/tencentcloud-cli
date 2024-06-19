**Example 1: 查询任务概览情况**



Input: 

```
tccli dlc DescribeTasksOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "923423423445",
        "TasksOverview": {
            "TaskQueuedCount": 0,
            "TaskInitCount": 0,
            "TaskRunningCount": 0,
            "TotalTaskCount": 0
        }
    }
}
```

