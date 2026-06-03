**Example 1: 查询**



Input: 

```
tccli cdwdoris DescribeBackUpSchedules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackUpOpened": true,
        "BackUpStatus": 0,
        "BackupScheduleInfos": [
            {
                "BackupType": 0,
                "BucketEncryption": {
                    "EncryptionType": "disabled",
                    "IsEncrypted": false,
                    "LastOperation": "",
                    "LastUpdateTime": ""
                },
                "BucketType": "standard",
                "CosSourceInfo": "dNWAedGPDTTCZjC95G2i5A==",
                "DataRemoteRegion": "",
                "DorisSourceInfo": "dNWAedGPDTTCZjC95G2i5A==",
                "EnableSecurityLock": 0,
                "ExistCount": 1,
                "GracePeriod": 0,
                "GraceStartTime": "",
                "InstanceId": "cdwdoris-wmkiloz9",
                "InstanceName": "liuming-yunti-test2",
                "InstanceStatus": "Serving",
                "InstanceStatusDesc": "运行中",
                "IsWithinGracePeriod": true,
                "RestoreType": 0,
                "SnapshotRemainPolicy": {
                    "RemainDays": 0,
                    "RemainDaysUnit": 0,
                    "RemainLatestNum": 0,
                    "Type": 0
                }
            }
        ],
        "CosBucketName": "",
        "CurrentTime": "2026-03-12 19:09:36",
        "RequestId": "3bf34b8b-bac3-4474-ad5d-631664d70fb3"
    }
}
```

