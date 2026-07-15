**Example 1: 删除日志下载任务**



Input: 

```
tccli sqlserver DeleteExportTask --cli-unfold-argument  \
    --LogType auditLog \
    --FileName mssql-8eei3sy5_20260316-124617_to_20260316-154617_1773647182589.tar.gz \
    --InstanceId mssql-8lv5ti3v
```

Output: 
```
{
    "Response": {
        "RequestId": "c753537d-f095-455b-ace1-6c0790a3ab2d"
    }
}
```

