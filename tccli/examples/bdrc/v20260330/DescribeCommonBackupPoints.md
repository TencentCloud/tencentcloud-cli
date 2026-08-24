**Example 1: 查询共同备份点**



Input: 

```
tccli bdrc DescribeCommonBackupPoints --cli-unfold-argument  \
    --InstanceIds ins-mpd1f3mq
```

Output: 
```
{
    "Response": {
        "CommonBackupPointSet": [
            {
                "BackupCommonTime": "2026-06-09T19:00:00+08:00",
                "BackupDetailSet": [
                    {
                        "BackupBindDisk": [
                            {
                                "BackupId": "backup-515yr2uf",
                                "DiskId": "disk-qadf2ekm"
                            }
                        ],
                        "BackupId": "cbackup-nb7fb5wh",
                        "CreateTime": "2026-06-09T19:00:18+08:00",
                        "InstanceId": "ins-mpd1f3mq"
                    }
                ]
            }
        ],
        "TotalCount": 4,
        "RequestId": "b395ed79-c79b-432d-aefd-1291b78bf07d"
    }
}
```

