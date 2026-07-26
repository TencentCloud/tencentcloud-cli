**Example 1: 查询实例归档日志列表**

查询实例归档日志列表信息

Input: 

```
tccli tdmysql DescribeDBSArchiveLogs --cli-unfold-argument  \
    --InstanceId tdsql3-000d02ac \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ArchiveLogId": 7365,
                "BackupDuration": 59610,
                "BackupStatus": "success",
                "EndTime": "2025-07-31 16:02:34",
                "ErrorMessage": "",
                "ExpiredTime": "2025-08-07 16:02:34",
                "FileName": "2025-07-31",
                "FileSize": 397689856,
                "InstanceId": "tdsql3-000d02ac",
                "StartTime": "2025-07-30 23:42:34"
            }
        ],
        "RequestId": "e8f0457c-f287-45a0-b45f-a5be3ef7a30b",
        "TotalCount": 8
    }
}
```

