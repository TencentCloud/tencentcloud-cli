**Example 1: 查询备份概览信息**



Input: 

```
tccli bdrc DescribeBackupOverviewGeneral --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupPolicyOverview": {
            "BoundCount": 8,
            "TotalCount": 45,
            "UnboundCount": 37
        },
        "BackupVaultOverview": {
            "TotalCount": 16,
            "TotalSizeMb": 118031
        },
        "FileBackupOverview": {
            "BackupCount": 20,
            "BackupResourceCount": 5,
            "BackupSizeMb": 118031,
            "CreatingBackupCount": 3,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 1,
            "SuccessBackupCount": 16
        },
        "InstanceBackupOverview": {
            "BackupCount": 217,
            "BackupResourceCount": 9,
            "BackupSizeMb": 67225600,
            "CreatingBackupCount": 0,
            "FailedBackupCount": 0,
            "RestoringBackupCount": 0,
            "SuccessBackupCount": 217
        },
        "ProtectedResourceOverview": {
            "CFS": {
                "ProtectedCount": 12,
                "TotalCount": 8
            },
            "Cvm": {
                "ProtectedCount": 9,
                "TotalCount": 8
            },
            "TotalProtectedCount": 21,
            "TotalResourceCount": 16
        },
        "RequestId": "89bb101d-133d-48a9-abec-98c857e031aa"
    }
}
```

