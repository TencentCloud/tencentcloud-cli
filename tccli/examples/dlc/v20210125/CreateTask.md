**Example 1: 创建sql任务**



Input: 

```
tccli dlc CreateTask --cli-unfold-argument  \
    --Task.SQLTask.SQL xx \
    --DatabaseName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskId": "xx"
    }
}
```

