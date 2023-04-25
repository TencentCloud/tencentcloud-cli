**Example 1: 查询广州二区状态为NORMAL的快照**

查询广州二区状态为NORMAL的快照

Input: 

```
tccli cbs DescribeSnapshots --cli-unfold-argument  \
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
        "RequestId": "7974489b-8d50-4bbd-8dd2-b700bb98b8cf",
        "SnapshotSet": [
            {
                "Tags": [],
                "Placement": {
                    "CageId": "",
                    "Zone": "ap-guangzhou-2",
                    "ProjectId": 0,
                    "CdcName": "",
                    "CdcId": "",
                    "ProjectName": "",
                    "DedicatedClusterId": ""
                },
                "CopyFromRemote": false,
                "IsPermanent": true,
                "DiskUsage": "DATA_DISK",
                "DeadlineTime": "2023-04-09 10:45:11",
                "Percent": 100,
                "SnapshotId": "snap-0jfkjwl1",
                "ShareReference": 0,
                "SnapshotType": "PRIVATE_SNAPSHOT",
                "DiskSize": 70,
                "DiskId": "disk-omp7wl2m",
                "SnapshotName": "TEST",
                "Images": [],
                "CopyingToRegions": [],
                "Encrypt": false,
                "CreateTime": "2023-03-09 10:45:11",
                "TimeStartShare": "2023-03-09",
                "ImageCount": 0,
                "SnapshotState": "NORMAL"
            },
            {
                "Tags": [],
                "Placement": {
                    "CageId": "",
                    "Zone": "ap-guangzhou-2",
                    "ProjectId": 0,
                    "CdcName": "",
                    "CdcId": "",
                    "ProjectName": "",
                    "DedicatedClusterId": ""
                },
                "CopyFromRemote": false,
                "IsPermanent": true,
                "DiskUsage": "SYSTEM_DISK",
                "DeadlineTime": "2023-04-09 10:45:11",
                "Percent": 100,
                "SnapshotId": "snap-obgelzpb",
                "ShareReference": 0,
                "SnapshotType": "PRIVATE_SNAPSHOT",
                "DiskSize": 50,
                "DiskId": "disk-1en5p0sq",
                "SnapshotName": "test-stevenkli",
                "Images": [],
                "CopyingToRegions": [],
                "Encrypt": false,
                "CreateTime": "2023-03-08 17:12:42",
                "ImageCount": 0,
                "TimeStartShare": "2023-03-09",
                "SnapshotState": "NORMAL"
            }
        ]
    }
}
```

