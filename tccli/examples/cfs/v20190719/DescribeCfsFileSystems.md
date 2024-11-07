**Example 1: 查询文件系统**

查询文件系统

Input: 

```
tccli cfs DescribeCfsFileSystems --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "FileSystems": [
            {
                "CreationTime": "abc",
                "CreationToken": "abc",
                "FileSystemId": "abc",
                "LifeCycleState": "abc",
                "SizeByte": 1,
                "SizeLimit": 1,
                "ZoneId": 1,
                "Zone": "abc",
                "Protocol": "abc",
                "StorageType": "abc",
                "StorageResourcePkg": "abc",
                "BandwidthResourcePkg": "abc",
                "PGroup": {
                    "PGroupId": "abc",
                    "Name": "abc"
                },
                "FsName": "abc",
                "Encrypted": true,
                "KmsKeyId": "abc",
                "AppId": 0,
                "BandwidthLimit": 0,
                "AutoSnapshotPolicyId": "abc",
                "SnapStatus": "abc",
                "Capacity": 1,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "TieringState": "abc",
                "TieringDetail": {
                    "TieringSizeInBytes": 0
                },
                "AutoScaleUpRule": {
                    "Status": "abc",
                    "ScaleThreshold": 1,
                    "TargetThreshold": 1
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

