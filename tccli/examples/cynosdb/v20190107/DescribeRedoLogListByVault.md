**Example 1: 查询保险箱下redoLog的列表**



Input: 

```
tccli cynosdb DescribeRedoLogListByVault --cli-unfold-argument  \
    --VaultId vault-a6ed23f2-f03e-4410-b946-624d1e7d9b5a
```

Output: 
```
{
    "Response": {
        "RedoLogList": [
            {
                "ClusterId": "cynosdbmysql-03e2xlyd",
                "ClusterName": "backupT_202602021239",
                "RedoFileInfo": {
                    "BackupTime": "1970-01-01 08:00:01",
                    "CopyStatus": "done",
                    "FileName": "backupT_202602021239_20260202153128",
                    "FileSize": 600941264,
                    "FinishTime": "1970-01-01 08:00:01",
                    "RedoCrossRegions": [],
                    "RedoLogId": 1282,
                    "StartTime": "1970-01-01 08:00:01",
                    "Status": "creating"
                }
            }
        ],
        "TotalCount": 2,
        "RequestId": "603b58ae-3e3e-41a7-9dcd-d0bf13044ce0"
    }
}
```

