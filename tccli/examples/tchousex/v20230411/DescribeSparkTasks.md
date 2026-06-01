**Example 1: DescribeSparkTasks**

获取spark task任务详情


Input: 

```
tccli tchousex DescribeSparkTasks --cli-unfold-argument  \
    --JobId abc \
    --StartTime abc \
    --EndTime abc \
    --Status 0 \
    --Limit 0 \
    --Offset 0
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
        "JobCreator": "abc",
        "RequestId": "abc"
    }
}
```

