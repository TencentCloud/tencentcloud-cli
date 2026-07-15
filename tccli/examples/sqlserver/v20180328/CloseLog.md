**Example 1: 关闭日志**



Input: 

```
tccli sqlserver CloseLog --cli-unfold-argument  \
    --InstanceId mssql-8lv5ti3v \
    --LogType auditLog
```

Output: 
```
{
    "Response": {
        "RequestId": "6807a5b4-ef25-480d-b77b-803d160e2603"
    }
}
```

