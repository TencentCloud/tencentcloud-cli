**Example 1: DescribeSparkTask**

查询spark 任务信息


Input: 

```
tccli tchousex DescribeSparkTask --cli-unfold-argument  \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "SparkTask": {
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
        },
        "RequestId": "abc"
    }
}
```

