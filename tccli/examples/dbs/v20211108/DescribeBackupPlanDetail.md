**Example 1: 备份计划详情**



Input: 

```
tccli dbs DescribeBackupPlanDetail --cli-unfold-argument  \
    --BackupPlanId dbs-6ll0ly4c
```

Output: 
```
{
    "Response": {
        "AllowedActions": [
            "view"
        ],
        "AutoRenewFlag": 0,
        "BackupObject": {
            "ObjectItems": null,
            "ObjectMode": "all"
        },
        "BackupPlanId": "dbs-6ll0ly4c",
        "BackupPlanName": "dbs-6ll0ly4c",
        "BackupStrategy": {
            "BackupMethod": "logical",
            "BackupPeriod": {
                "Day": [
                    "Monday"
                ],
                "PeriodType": "Weekly"
            },
            "BackupStartTime": "17:00",
            "EnableIncrement": true,
            "StorageStrategy": {
                "BackupRetentionPeriod": 8,
                "Encryption": "UnEncrypted",
                "FullStorageStrategy": {
                    "RetentionPeriod": 30,
                    "RetentionType": "",
                    "TieredStrategy": {
                        "DayToArchive": 0,
                        "DayToDeepArchive": 0,
                        "DayToLowFrequency": 0
                    }
                },
                "IncStorageStrategy": {
                    "RetentionPeriod": 30,
                    "RetentionType": "",
                    "TieredStrategy": {
                        "DayToArchive": 0,
                        "DayToDeepArchive": 0,
                        "DayToLowFrequency": 0
                    }
                },
                "StorageType": "system"
            },
            "StrategyType": "period"
        },
        "CreateTime": "2026-10-30 11:08:56",
        "ErrorInfo": {
            "ErrorMsg": "ok",
            "ErrorType": ""
        },
        "ExpireTime": "2026-11-30 11:08:56",
        "LastBackupJobTime": "",
        "LastFullBackupJobStatus": "",
        "LastIncBackupJobStatus": "",
        "LastRestoreJobStatus": "",
        "LastRestoreJobTime": "",
        "NextBackupJobTime": "",
        "OfflineTime": "2026-12-14 11:08:56",
        "PayInfo": {
            "CreateTime": "2026-10-30 11:08:56",
            "FreeSpace": 42949672960,
            "FullBackupSetSize": 0,
            "FullChargeSpace": 0,
            "IncrementBackupSetSize": 0,
            "IncrementChargeSpace": 0,
            "InstanceClass": "micro",
            "PayType": "prePay",
            "TimeRange": "2026-10-30 11:08:56 - 2026-10-30 11:10:12",
            "TotalChargeSpace": 0
        },
        "Progress": {
            "CurrentBackupJobStatus": "starting",
            "FullBackupStatus": "",
            "IncrementBackupStatus": "running",
            "LastBackupTime": "2026-10-30 11:10:11",
            "LastRestoreStatus": "",
            "LastRestoreTime": "",
            "NextBackupTime": "0000-00-00 00:00:00"
        },
        "Region": "ap-guangzhou",
        "RestoreRange": {
            "EndTime": "",
            "StartTime": ""
        },
        "SetSourceInfo": [],
        "SourceEndPoint": [
            {
                "AccessType": "cdb",
                "CcnId": "",
                "CvmInstanceId": "",
                "DBKernel": "",
                "DatabaseType": "mysql",
                "EngineVersion": "",
                "InstanceId": "cdb-favwofb9",
                "Ip": "",
                "Password": "",
                "Port": 0,
                "Region": "ap-guangzhou",
                "Role": "master",
                "SubnetId": "",
                "Supplier": "others",
                "UniqDcgId": "",
                "UniqVpnGwId": "",
                "UserName": "tencent",
                "VpcId": ""
            }
        ],
        "SourceInfo": [
            "cdb-favwofb9"
        ],
        "Status": "fullBacking",
        "Tags": null,
        "UpperBandwidth": 3,
        "UpperParallel": 2,
        "RequestId": "9e5315f0-64b2-4949-b808-e410e066c042"
    }
}
```

