**Example 1: 查询会话信息**



Input: 

```
tccli tchousex DescribeNotebookSession --cli-unfold-argument  \
    --SessionId livy-session-8pu64i
```

Output: 
```
{
    "Response": {
        "RequestId": "97335dd5-f3c7-4d2d-bb02-41cf8822686c",
        "ErrorMsg": "",
        "Session": {
            "InstanceId": "warehouse-hk9pr4ve",
            "SessionId": "livy-session-8pu64i",
            "Name": "session-1737381301",
            "Kind": "spark",
            "Jars": "",
            "PyFiles": "",
            "Files": "",
            "Archives": "",
            "State": "dead",
            "ExecutorCores": 4,
            "ExecutorNum": 1,
            "DriverCores": 4,
            "SparkUiUrl": "",
            "TimeoutInSecond": 3600
        }
    }
}
```

