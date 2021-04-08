**Example 1: 查看快照列表**



Input: 

```
tccli lighthouse DescribeSnapshots --cli-unfold-argument  \
    --Filters.0.Name disk-id \
    --Filters.0.Values lhdisk-f71kc5bh
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SnapshotSet": [
            {
                "SnapshotId": "lhsnap-nv6aqcv6",
                "DiskUsage": "SYSTEM_DISK",
                "DiskId": "lhdisk-f71kc5bh",
                "DiskSize": 50,
                "SnapshotName": "lighthouse-test1-0903145122",
                "SnapshotState": "NORMAL",
                "Percent": "100",
                "LatestOperation": "RollbackInstanceSnapshot",
                "LatestOperationState": "SUCCESS",
                "LatestOperationRequestId": "96aee6e3-172c-4f0f-be7c-fc46b9865763",
                "CreatedTime": "2020-09-03T06:51:23Z"
            }
        ],
        "RequestId": "95aacc96-b271-4d8b-bf83-019647952af9"
    }
}
```

