**Example 1: 查询文件系统**

查询文件系统

Input: 

```
tccli cfs DescribeCfsFileSystems --cli-unfold-argument  \
    --FileSystemId cfs-318f2b7ba
```

Output: 
```
{
    "Response": {
        "FileSystems": [
            {
                "AppId": 1300275735,
                "AutoScaleUpRule": {
                    "ScaleThreshold": 80,
                    "TargetThreshold": 70,
                    "Status": "open"
                },
                "AutoSnapshotPolicyId": "",
                "BandwidthLimit": 100,
                "BandwidthResourcePkg": "",
                "Capacity": 2097152,
                "CreationTime": "2024-07-09 10:52:35",
                "CreationToken": "denny-test-003",
                "Encrypted": false,
                "FileSystemId": "cfs-318f2b7ba",
                "FsName": "denny-test-003",
                "KmsKeyId": "",
                "LifeCycleState": "available",
                "PGroup": {
                    "Name": "默认权限组",
                    "PGroupId": "pgroupbasic"
                },
                "Protocol": "NFS",
                "SizeByte": 0,
                "SizeLimit": 1000000,
                "SnapStatus": "normal",
                "StorageResourcePkg": "",
                "StorageType": "SD",
                "Tags": [],
                "TieringDetail": {
                    "SecondaryTieringSizeInBytes": -1,
                    "TieringSizeInBytes": -1
                },
                "TieringState": "NotAvailable",
                "Zone": "ap-guangzhou-2",
                "ZoneId": 100002
            }
        ],
        "RequestId": "8edb5b83-6bd2-4f0a-8ee9-d8ee96fff8dc",
        "TotalCount": 1
    }
}
```

