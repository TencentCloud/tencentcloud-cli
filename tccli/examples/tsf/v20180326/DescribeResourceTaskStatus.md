**Example 1: 获取资源任务的执行状态**



Input: 

```
tccli tsf DescribeResourceTaskStatus --cli-unfold-argument  \
    --TaskId task-57xee9nb
```

Output: 
```
{
    "Response": {
        "RequestId": "d227ab41-d339-441c-a71a-89e4b8304716",
        "Result": {
            "TaskStatus": 2
        }
    }
}
```

