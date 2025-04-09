**Example 1: DescribeSparkSqlTasks**

查询spark sql任务列表

Input: 

```
tccli tchousex DescribeSparkSqlTasks --cli-unfold-argument  \
    --InstanceId abc \
    --StartTime abc \
    --EndTime abc \
    --Status 0 \
    --Limit 0 \
    --Offset 0 \
    --TaskName abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ErrorMsg": "abc",
        "SparkTaskList": [
            {
                "InstanceId": "abc",
                "JobId": "abc",
                "TaskId": "abc",
                "SparkArgs": "abc",
                "DriverPodName": "abc",
                "Creator": "abc",
                "Status": 0,
                "ExecutorCores": 0,
                "ExecutorNum": 0,
                "DriverCores": 0,
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "ExecuteTime": "abc",
                "Id": 0,
                "LivyBody": "abc",
                "ExecutorPodNames": "abc",
                "BatchId": 0,
                "BeginTime": "abc",
                "BillingTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

