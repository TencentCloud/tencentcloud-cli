**Example 1: 查询spark job 列表**

查询spark job 列表

Input: 

```
tccli tchousex DescribeSparkJobs --cli-unfold-argument  \
    --InstanceId abc \
    --SparkMsg abc \
    --StartTime abc \
    --EndTime abc \
    --Limit 0 \
    --Offset 0 \
    --JobId abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ErrorMsg": "abc",
        "SparkJobList": [
            {
                "InstanceId": "abc",
                "JobId": "abc",
                "SparkName": "abc",
                "File": "abc",
                "ClassName": "abc",
                "Args": "abc",
                "Configs": "abc",
                "Jars": "abc",
                "PyFiles": "abc",
                "Files": "abc",
                "Archives": "abc",
                "Creator": "abc",
                "Status": 0,
                "ExecutorCores": 1,
                "ExecutorNum": 1,
                "DriverCores": 1,
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "CurrentTaskNum": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

