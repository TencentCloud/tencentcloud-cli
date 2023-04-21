**Example 1: 创建审计日志文件**

创建审计日志文件生成任务

Input: 

```
tccli dbbrain CreateAuditLogFile --cli-unfold-argument  \
    --Product dcdb \
    --NodeRequestType dcdb \
    --InstanceId cdb-qwerasdf \
    --StartTime 2020-09-22T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": 64,
        "RequestId": "a5039c90-d83f-11ed-a995-6d91182a5559"
    }
}
```

