**Example 1: 查询备份下载任务**



Input: 

```
tccli mongodb DescribeBackupDownloadTask --cli-unfold-argument  \
    --InstanceId cmgo-fdzf**** \
    --Status 2
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c0c495-4826-4938-a6d7-32146cad2632",
        "Tasks": [
            {
                "BackupDesc": "系统后台每日定时自动备份",
                "BackupMethod": 0,
                "BackupName": "cmgo-fdzf****_2025-09-23 22:03",
                "BackupSize": 5747378,
                "Bucket": "sh-backup-remote-125758****",
                "CreateTime": "2025-09-24 10:58:55",
                "Percent": 100,
                "Region": "ap-shanghai",
                "ReplicaSetId": "cmgo-fdzf******",
                "Status": 2,
                "TimeSpend": 1,
                "Url": "https://sh-backup-remote-tar-**************"
            }
        ],
        "TotalCount": 1
    }
}
```

