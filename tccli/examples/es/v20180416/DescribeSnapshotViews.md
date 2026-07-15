**Example 1: demo**



Input: 

```
tccli es DescribeSnapshotViews --cli-unfold-argument  \
    --InstanceId es-ldmd4rpp \
    --State SUCCESS \
    --UserBackUp false \
    --Duration 0
```

Output: 
```
{
    "Response": {
        "Snapshots": [
            {
                "AutoBackupInterval": 1,
                "CosEncryption": 0,
                "CosRetention": 0,
                "DataStreams": [
                    "ilm-history-5"
                ],
                "DurationInMillis": 42616,
                "EndTime": "2026-04-20T09:53:01.383Z",
                "EsRepositoryType": 0,
                "FailedShards": 0,
                "Failures": [],
                "Indices": [
                    ".apm-agent-configuration"
                ],
                "InstanceId": "es-ldmd4rpp",
                "IsLocked": 0,
                "KmsKey": "",
                "MultiAz": 0,
                "PaasEsRepository": "ES_AUTO_BACKUP_cosbackup4294967516",
                "RemoteCos": 0,
                "RemoteCosRegion": "ap-guangzhou",
                "Repository": "ES_AUTO_BACKUP_cosbackup4294967516",
                "RetainUntilDate": "",
                "RetentionGraceTime": 0,
                "SnapshotName": "test2-hour-snapshot_20260420_17",
                "StartTime": "2026-04-20T09:52:18.767Z",
                "State": "SUCCESS",
                "StorageDuration": 7,
                "StrategyName": "test2-hour",
                "SuccessfulShards": 14,
                "TotalShards": 14,
                "UserBackUp": "false",
                "UserEsRepository": "",
                "Uuid": "BI8atOQtRoO5p4BZSgX0OA",
                "Version": "7.14.2"
            }
        ],
        "RequestId": "378df927-e4af-4950-a521-29d72846cc23"
    }
}
```

