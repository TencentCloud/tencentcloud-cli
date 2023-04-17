**Example 1: 获取迁移任务列表**

用于获取迁移任务列表

Input: 

```
tccli cfs DescribeMigrationTasks --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "MigrationTasks": [
            {
                "TaskName": "taskName",
                "TaskId": "cfsmigrate-29d43e98",
                "MigrationType": 0,
                "MigrationMode": 0,
                "BucketName": "bucket-1",
                "BucketRegion": "oss-cn-beijing",
                "BucketAddress": "https://test-1.oss-cn-beijing.aliyuncs.com",
                "BucketPath": "",
                "ListAddress": "",
                "FsName": "t1",
                "FileSystemId": "cfs-qz5c44o1",
                "FsPath": "/ahh",
                "CoverType": 0,
                "Status": 6,
                "FileTotalCount": 0,
                "FileMigratedCount": 0,
                "FileFailedCount": 0,
                "FileTotalSize": 0,
                "FileMigratedSize": 0,
                "FileFailedSize": 0,
                "FileTotalList": null,
                "FileCompletedList": null,
                "FileFailedList": null,
                "CreateTime": 1662023240000,
                "EndTime": 1662023548000
            }
        ],
        "TotalCount": 2,
        "RequestId": "c0f7c5d9-c8c4-401a-a6da-2106f3c6db76"
    }
}
```

