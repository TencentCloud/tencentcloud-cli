**Example 1: 查询错误日志**

查询错误日志

Input: 

```
tccli cynosdb DescribeInstanceErrorLogs --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-m6f0hkkd \
    --Limit 1 \
    --Offset 0 \
    --StartTime 2024-10-28 10:19:21 \
    --EndTime 2024-10-28 10:20:01 \
    --OrderBy Timestamp \
    --OrderByType DESC \
    --LogLevels note \
    --KeyWords unconnected
```

Output: 
```
{
    "Response": {
        "ErrorLogs": [
            {
                "Content": "Aborted connection 562579 to db: 'unconnected' user: 'unauthenticated' host: '169.214.18.1' (Got an error reading communication packets)",
                "Level": "note",
                "Timestamp": 1730182001
            }
        ],
        "RequestId": "32f291cb-38c8-4a0c-8fd0-5a4c370ac6df",
        "TotalCount": 3
    }
}
```

