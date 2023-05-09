**Example 1: 查询错误日志**

查询错误日志

Input: 

```
tccli cynosdb DescribeInstanceErrorLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-xxxxxxxx \
    --Limit 10 \
    --Offset 0 \
    --StartTime 2019-07-04 16:45:32 \
    --EndTime 2019-07-04 16:55:32 \
    --OrderBy Timestatmp \
    --OrderByType DESC \
    --LogLevels error \
    --KeyWords abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ErrorLogs": [
            {
                "Timestamp": 0,
                "Level": "error",
                "Content": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

