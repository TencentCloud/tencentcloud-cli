**Example 1: redo日志列表**

Describe Redo Logs

Input: 

```
tccli cynosdb DescribeRedoLogs --cli-unfold-argument  \
    --ClusterId cynosdbmysql-gfo7ejhl \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RedoLogs": [
            {
                "BackupTime": "2025-09-22 14:35:44",
                "FileName": "backupT_lowcase_202509221241_20250922143544",
                "FileSize": 738914945,
                "FinishTime": "2025-09-22 14:36:44",
                "RedoCrossRegions": [
                    {
                        "BackupId": 22822,
                        "BackupRegion": "ap-guangzhou"
                    }
                ],
                "RedoLogId": 22822,
                "StartTime": "2025-09-22 14:35:44",
                "Status": "success"
            },
            {
                "BackupTime": "2025-09-22 14:18:22",
                "FileName": "backupT_lowcase_202509221241_20250922141822",
                "FileSize": 739166672,
                "FinishTime": "2025-09-22 14:19:23",
                "RedoCrossRegions": [
                    {
                        "BackupId": 22818,
                        "BackupRegion": "ap-guangzhou"
                    }
                ],
                "RedoLogId": 22818,
                "StartTime": "2025-09-22 14:18:22",
                "Status": "success"
            }
        ],
        "RequestId": "813bd72c-a8c4-4e99-badf-0136e8e6ba89",
        "TotalCount": 12
    }
}
```

