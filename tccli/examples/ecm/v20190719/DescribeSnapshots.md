**Example 1: 查询广州二区状态为NORMAL的快照**



Input: 

```
tccli ecm DescribeSnapshots --cli-unfold-argument  \
    --Filters.0.Name snapshot-state \
    --Filters.0.Values NORMAL \
    --Filters.1.Name zone \
    --Filters.1.Values ap-guangzhou-2
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "4ab150b9-538d-48fb-8821-7fa185f1d07c",
        "SnapshotSet": [
            {
                "Placement": {
                    "ProjectId": 0,
                    "Zone": "ap-guangzhou-2"
                },
                "TimeStartShare": "2020-09-22",
                "CopyFromRemote": false,
                "IsPermanent": false,
                "DiskUsage": "DATA_DISK",
                "DeadlineTime": "2019-07-15 00:00:00",
                "Percent": 100,
                "SnapshotId": "snap-lfo7xxxx",
                "ShareReference": 0,
                "SnapshotType": "PRIVATE_SNAPSHOT",
                "DiskSize": 10,
                "DiskId": "disk-aq3k1jn0",
                "SnapshotName": "auto_disk-aq3k1jn0_20190708_00",
                "Images": [],
                "CopyingToRegions": [],
                "Encrypt": false,
                "CreateTime": "2019-07-08 00:03:13",
                "ImageCount": 0,
                "SnapshotState": "NORMAL"
            },
            {
                "Placement": {
                    "ProjectId": 0,
                    "Zone": "ap-guangzhou-2"
                },
                "TimeStartShare": "2020-09-22",
                "CopyFromRemote": false,
                "IsPermanent": false,
                "DiskUsage": "DATA_DISK",
                "DeadlineTime": "2019-07-15 00:00:00",
                "Percent": 100,
                "SnapshotId": "snap-jt5nxxxx",
                "ShareReference": 0,
                "SnapshotType": "PRIVATE_SNAPSHOT",
                "DiskSize": 10,
                "DiskId": "disk-38hlz2p0",
                "SnapshotName": "auto_disk-38hlz2p0_20190708_00",
                "Images": [],
                "CopyingToRegions": [],
                "Encrypt": false,
                "CreateTime": "2019-07-08 00:03:10",
                "ImageCount": 0,
                "SnapshotState": "NORMAL"
            }
        ]
    }
}
```

