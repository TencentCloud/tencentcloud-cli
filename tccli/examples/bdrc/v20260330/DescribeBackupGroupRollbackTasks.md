**Example 1: 查询备份组恢复任务**



Input: 

```
tccli bdrc DescribeBackupGroupRollbackTasks --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RollbackTaskSet": [
            {
                "AppId": 251246004,
                "BackupGroupId": "cbackup-n3thksnh",
                "BackupGroupName": "kairoslliu_test_bakcupgroup",
                "EndTime": "2026-06-10T15:19:14+08:00",
                "FailReason": "",
                "Percent": 100,
                "RollbackType": "ORIGINAL",
                "SourceInstanceId": "ins-jzqjqa8a",
                "StartTime": "2026-06-10T15:18:15+08:00",
                "Status": "done",
                "TargetInstanceId": "ins-jzqjqa8a",
                "TaskId": "crollback-788qdm6d"
            }
        ],
        "TotalCount": 3,
        "RequestId": "071ed354-2566-497b-993d-e559493146ca"
    }
}
```

