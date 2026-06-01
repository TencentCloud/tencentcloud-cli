**Example 1: 查询spark job 详情**



Input: 

```
tccli tchousex DescribeSparkJob --cli-unfold-argument  \
    --JobId 123
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "abc",
        "SparkJob": {
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
            "CurrentTaskNum": 1,
            "CurrentTaskId": "abc",
            "ID": 0,
            "ExtInfo": "abc",
            "Source": 0
        },
        "RequestId": "abc"
    }
}
```

