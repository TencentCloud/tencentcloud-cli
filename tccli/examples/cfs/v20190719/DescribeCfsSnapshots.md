**Example 1: 查询快照**



Input: 

```
tccli cfs DescribeCfsSnapshots --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Snapshots": [
            {
                "CreationTime": "abc",
                "SnapshotName": "abc",
                "SnapshotId": "abc",
                "Status": "abc",
                "RegionName": "abc",
                "FileSystemId": "abc",
                "Size": 1,
                "AliveDay": 1,
                "Percent": 1,
                "AppId": 1,
                "DeleteTime": "abc",
                "FsName": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "SnapshotType": "abc",
                "SnapshotTime": "abc"
            }
        ],
        "TotalSize": 1,
        "RequestId": "abc"
    }
}
```

