**Example 1: 查询云数据库实例的备份文件信息**



Input: 

```
tccli mongodb DescribeDBBackups --cli-unfold-argument  \
    --InstanceId cmgo-fdzf**** \
    --BackupMethod 0
```

Output: 
```
{
    "Response": {
        "BackupList": [
            {
                "BackId": 10657020,
                "BackupDesc": "系统后台每日定时自动备份",
                "BackupMethod": 0,
                "BackupName": "cmgo-fdzf****_2025-09-17 22:01",
                "BackupRegion": "",
                "BackupSize": 5747379,
                "BackupType": 0,
                "DeleteTime": "2025-09-24 22:01:58",
                "EndTime": "2025-09-17 22:01:58",
                "InstanceId": "cmgo-fdzf****",
                "RestoreTime": "",
                "StartTime": "2025-09-17 22:01:52",
                "Status": 2
            },
            {
                "BackId": 10688339,
                "BackupDesc": "系统后台每日定时自动备份",
                "BackupMethod": 0,
                "BackupName": "cmgo-fdzf****_2025-09-18 22:03",
                "BackupRegion": "ap-shanghai",
                "BackupSize": 5747378,
                "BackupType": 0,
                "DeleteTime": "2025-09-20 22:03:37",
                "EndTime": "2025-09-18 22:03:44",
                "InstanceId": "cmgo-fdzf****",
                "RestoreTime": "",
                "StartTime": "2025-09-18 22:03:42",
                "Status": 2
            }
        ],
        "RequestId": "0e2eb0e1-f775-4ba8-af9f-e5650a55dce1",
        "TotalCount": 2
    }
}
```

