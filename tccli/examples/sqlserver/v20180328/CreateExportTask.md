**Example 1: 创建日志下载任务**



Input: 

```
tccli sqlserver CreateExportTask --cli-unfold-argument  \
    --InstanceId mssql-8lv5ti3v \
    --LogType auditLog \
    --StartTime 2025-08-14 16:24:24 \
    --EndTime 2026-08-14 16:24:24
```

Output: 
```
{
    "Response": {
        "RequestId": "f210476a-a621-4bf2-95a9-cd3d6a4dbde5"
    }
}
```

