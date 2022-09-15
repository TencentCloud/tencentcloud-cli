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
        "TotalSize": 1,
        "TotalCount": 1,
        "RequestId": "xx",
        "Snapshots": [
            {
                "Status": 1,
                "SnapshotName": "xx",
                "Percent": 1,
                "FileSystemId": "xx",
                "Size": 1,
                "AppId": 1,
                "SnapshotId": "xx",
                "AliveDay": 1,
                "CreationTime": "xx",
                "DeleteTime": "xx",
                "FsName": "xx",
                "RegionName": "xx"
            }
        ]
    }
}
```

