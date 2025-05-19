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
        "RequestId": "dd01b47d-2b57-4721-a237-1bdf59eac8b4",
        "Snapshots": [
            {
                "AliveDay": 0,
                "AppId": 1300275735,
                "CreationTime": "2024-09-27 16:03:06",
                "DeleteTime": "0",
                "FileSystemId": "cfs-12345",
                "FsName": "aileen-api-charge",
                "Percent": 0,
                "RegionName": "ap-guangzhou",
                "Size": 0,
                "SnapshotId": "snapcfs-5v2hgj3p",
                "SnapshotName": "heihei",
                "SnapshotTime": "2024-09-27 16:03:06",
                "SnapshotType": "Standard",
                "Status": "creating",
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "TotalSize": 0
    }
}
```

