**Example 1: 创建审计日志文件**



Input: 

```
tccli mongodb CreateAuditLogFile --cli-unfold-argument  \
    --InstanceId cmgo-qwer**** \
    --StartTime 2021-07-12 10:29:20 \
    --EndTime 2021-07-13 15:29:20
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

