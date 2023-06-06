**Example 1: 查询文件系统**



Input: 

```
tccli cfs DescribeCfsFileSystems --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "TotalCount": 1,
        "FileSystems": [
            {
                "Protocol": "NFS",
                "Zone": "ap-guangzhou-3",
                "CreationToken": "test_fs",
                "StorageType": "SD",
                "Encrypted": false,
                "CreationTime": "2019-07-29 18:57:17",
                "StorageResourcePkg": "",
                "ZoneId": 100003,
                "SizeByte": 0,
                "FileSystemId": "cfs-12345",
                "KmsKeyId": "",
                "LifeCycleState": "mounting",
                "Capacity": 1000,
                "PGroup": {
                    "PGroupId": "pgroupbasic",
                    "Name": "默认权限组"
                },
                "SizeLimit": 0,
                "BandwidthResourcePkg": "",
                "FsName": "test_fs",
                "AppId": 12700000,
                "BandwidthLimit": 200,
                "TieringDetail": {
                    "TieringSizeInBytes": 0
                },
                "TieringState": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ]
            }
        ]
    }
}
```

