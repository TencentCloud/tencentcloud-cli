**Example 1: 创建并执行SQL任务**

创建并执行SQL任务

Input: 

```
tccli dlc CreateTask --cli-unfold-argument  \
    --Task.SQLTask.SQL U0VMRUNUICogRlJPTSBgdGVzdGh5d2AuYHRlc3QxMDBtYCBMSU1JVCAxMDs= \
    --Task.SQLTask.Config.0.Key  \
    --Task.SQLTask.Config.0.Value  \
    --Task.SparkSQLTask.SQL  \
    --Task.SparkSQLTask.Config.0.Key spark.sql.sources.partitionOverwriteMode \
    --Task.SparkSQLTask.Config.0.Value static \
    --DatabaseName testdb
```

Output: 
```
{
    "Response": {
        "RequestId": "13bfd2b2-b92e-4c49-9c7e-3662b5f32165",
        "TaskId": "4ad30ca9-*-*-*-*"
    }
}
```

