**Example 1: 查询备份概览信息**



Input: 

```
tccli bdrc DescribeBackupOverviewGeneral --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupPolicyOverview": {
            "BoundCount": 21,
            "TotalCount": 146,
            "UnboundCount": 125
        },
        "BackupVaultOverview": {
            "TotalCount": 50,
            "TotalSizeMb": 8
        },
        "CFSAgentBackupOverview": {
            "BackupCount": 182,
            "BackupResourceCount": 0,
            "BackupSizeMb": 0,
            "CreatingBackupCount": 1,
            "FailedBackupCount": 154,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 16
        },
        "COSAgentBackupOverview": {
            "BackupCount": 228,
            "BackupResourceCount": 7,
            "BackupSizeMb": 8,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 73,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 153
        },
        "FileBackupOverview": {
            "BackupCount": 15,
            "BackupResourceCount": 0,
            "BackupSizeMb": 0,
            "CreatingBackupCount": 3,
            "FailedBackupCount": 8,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 2
        },
        "InstanceBackupOverview": {
            "BackupCount": 246,
            "BackupResourceCount": 12,
            "BackupSizeMb": 67319528,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 246
        },
        "ProtectedResourceOverview": {
            "CFS": {
                "ProtectedCount": 10,
                "TotalCount": 12
            },
            "CFSAgent": {
                "ProtectedCount": 3,
                "TotalCount": 14
            },
            "COSAgent": {
                "ProtectedCount": 15,
                "TotalCount": 31
            },
            "Cvm": {
                "ProtectedCount": 12,
                "TotalCount": 12
            },
            "TotalProtectedCount": 40,
            "TotalResourceCount": 69
        },
        "RequestId": "0f99c423-ef91-4c77-9c07-58ad635e2095"
    }
}
```

