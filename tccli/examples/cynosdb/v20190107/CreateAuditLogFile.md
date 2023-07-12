**Example 1: 创建审计日志文件**

创建审计日志文件

Input: 

```
tccli cynosdb CreateAuditLogFile --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf \
    --StartTime 2017-07-12 10:29:20 \
    --EndTime 2017-07-13 10:29:20
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "FileName": "test.csv"
    }
}
```

