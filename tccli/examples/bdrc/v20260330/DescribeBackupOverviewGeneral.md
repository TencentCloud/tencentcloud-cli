**Example 1: 查询备份概览信息**



Input: 

```
tccli bdrc DescribeBackupOverviewGeneral --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupPolicyOverview": {
            "BoundCount": 12,
            "TotalCount": 25,
            "UnboundCount": 13
        },
        "BackupVaultOverview": {
            "TotalCount": 13,
            "TotalSizeMb": 85233
        },
        "CFSAgentBackupOverview": {
            "BackupCount": 571,
            "BackupResourceCount": 7,
            "BackupSizeMb": 8303,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 44,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 527
        },
        "COSAgentBackupOverview": {
            "BackupCount": 89,
            "BackupResourceCount": 4,
            "BackupSizeMb": 583,
            "CreatingBackupCount": 1,
            "FailedBackupCount": 71,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 17
        },
        "FileBackupOverview": {
            "BackupCount": 18,
            "BackupResourceCount": 0,
            "BackupSizeMb": 72422,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 11,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 7
        },
        "InstanceBackupOverview": {
            "BackupCount": 9,
            "BackupResourceCount": 7,
            "BackupSizeMb": 51994,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 9
        },
        "LocalCFSAgentBackupOverview": {
            "BackupCount": 8,
            "BackupResourceCount": 4,
            "BackupSizeMb": 24411,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 8
        },
        "LocalCVMAgentBackupOverview": {
            "BackupCount": 2,
            "BackupResourceCount": 1,
            "BackupSizeMb": 3927,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 2
        },
        "ProtectedResourceOverview": {
            "CFS": {
                "ProtectedCount": 2,
                "TotalCount": 2
            },
            "CFSAgent": {
                "ProtectedCount": 17,
                "TotalCount": 28
            },
            "COSAgent": {
                "ProtectedCount": 10,
                "TotalCount": 13
            },
            "Cvm": {
                "ProtectedCount": 7,
                "TotalCount": 2
            },
            "LocalCFSAgent": {
                "ProtectedCount": 0,
                "TotalCount": 0
            },
            "LocalCVMAgent": {
                "ProtectedCount": 652,
                "TotalCount": 652
            },
            "TotalProtectedCount": 688,
            "TotalResourceCount": 697
        },
        "RequestId": "43889a89-698c-4926-a35f-d7f979882f54"
    }
}
```

