**Example 1: DescribeSnapshots**



Input: 

```
tccli cvd DescribeSnapshots --cli-unfold-argument  \
    --Filters.0.Values disk-nyz5l4i0 \
    --Filters.0.Name DiskId \
    --PageNumber 1 \
    --PageSize 20 \
    --SnapshotRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "SnapshotList": [
            {
                "LastRollbackTime": "2026-10-10 02:00:00",
                "IsPermanent": true,
                "DeadlineTime": "2026-10-24 02:00:00",
                "Percent": 100,
                "CreateType": "AutoSnapshot",
                "LastRollbackState": "SUCCESS",
                "DiskId": "disk-nyz5l4i0",
                "DiskUsage": "SYSTEM_DISK",
                "SnapshotId": "snap-1mehmi29",
                "CreateTime": "2026-10-21 02:14:52",
                "SnapshotState": "SUCCESS"
            }
        ],
        "TotalCount": 1,
        "RequestId": "2bcfe8b7-8ea8-4488-9d17-f1aeb106eecd"
    }
}
```

