**Example 1: 删除审计日志文件**

删除审计日志文件

Input: 

```
tccli dbbrain DeleteAuditLogFile --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --InstanceId tdsql-cerses \
    --AsyncRequestId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

