**Example 1: 查询文件备份恢复任务列表**



Input: 

```
tccli bdrc DescribeFileRestoreTasks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9a60051d-a34f-47ef-8578-db41c3297533",
        "RestoreTaskSet": [
            {
                "BackupId": "fb-op7apew4",
                "CreatedTime": "2026-03-31T21:36:08",
                "EndTime": "2026-03-31T21:36:49",
                "JobId": "j-20260331133609-7fcf71f2",
                "Progress": 100,
                "ResourceId": "ins-7630gzfm",
                "RestoreFileCount": 0,
                "RestorePaths": [
                    "/data"
                ],
                "RestoreSize": 0,
                "RestoreSizeFormatted": "0 B",
                "StartTime": "",
                "Status": "success",
                "TargetLocation": "/data1",
                "TargetResourceId": "ins-eej84hs4",
                "TaskId": "frt-0qu9s8ec",
                "TotalFileCount": 0,
                "TotalSize": 0,
                "TotalSizeFormatted": "0 B"
            },
            {
                "BackupId": "fb-p7xd1l0k",
                "CreatedTime": "2026-03-31T18:04:56",
                "EndTime": "2026-03-31T18:06:16",
                "JobId": "j-20260331100457-df0ca872",
                "Progress": 100,
                "ResourceId": "ins-7630gzfm",
                "RestoreFileCount": 0,
                "RestorePaths": [
                    "/data"
                ],
                "RestoreSize": 0,
                "RestoreSizeFormatted": "0 B",
                "StartTime": "",
                "Status": "success",
                "TargetLocation": "/data1",
                "TargetResourceId": "ins-7630gzfm",
                "TaskId": "frt-26k507t2",
                "TotalFileCount": 0,
                "TotalSize": 0,
                "TotalSizeFormatted": "0 B"
            },
            {
                "BackupId": "fb-p7xd1l0k",
                "CreatedTime": "2026-03-31T17:38:44",
                "EndTime": "2026-03-31T17:39:46",
                "JobId": "j-20260331093845-f371f289",
                "Progress": 100,
                "ResourceId": "ins-7630gzfm",
                "RestoreFileCount": 0,
                "RestorePaths": [
                    "data"
                ],
                "RestoreSize": 0,
                "RestoreSizeFormatted": "0 B",
                "StartTime": "",
                "Status": "success",
                "TargetLocation": "/data1",
                "TargetResourceId": "ins-7630gzfm",
                "TaskId": "frt-lsi51aiq",
                "TotalFileCount": 0,
                "TotalSize": 0,
                "TotalSizeFormatted": "0 B"
            }
        ],
        "TotalCount": 3
    }
}
```

