**Example 1: 创建sql任务**



Input: 

```
tccli dlc CreateTask --cli-unfold-argument  \
    --Task.SQLTask.SQL xx \
    --Task.SQLTask.Config.0.Key xx \
    --Task.SQLTask.Config.0.Value xx \
    --Task.SparkSQLTask.SQL xx \
    --Task.SparkSQLTask.Config.0.Key xx \
    --Task.SparkSQLTask.Config.0.Value xx \
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

