**Example 1: DescribeNodeResourceConfigFast示例**



Input: 

```
tccli emr DescribeNodeResourceConfigFast --cli-unfold-argument  \
    --InstanceId emr-laoxdz4n \
    --ResourceType ALL \
    --PayMode 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ResourceData": [
                    {
                        "CreateTime": "2024-03-25 17:52:23",
                        "IsDefault": "DEFAULT",
                        "MaxResourceNum": 0,
                        "Resource": {
                            "Cpu": 4,
                            "DiskNum": 1,
                            "DiskSize": 200,
                            "DiskType": "CLOUD_SSD",
                            "InstanceType": "SA2.LARGE8",
                            "LocalDiskNum": 0,
                            "MemSize": 8192,
                            "MultiDisks": [],
                            "RootSize": 70,
                            "Spec": "CVM.SA2",
                            "StorageType": 4,
                            "Tags": null
                        },
                        "ResourceConfigId": 20332,
                        "UpdateTime": "2024-03-25 17:52:23"
                    }
                ],
                "ResourceType": "CORE"
            },
            {
                "ResourceData": [
                    {
                        "CreateTime": "2024-04-08 15:13:04",
                        "IsDefault": "DEFAULT",
                        "MaxResourceNum": 0,
                        "Resource": {
                            "Cpu": 8,
                            "DiskNum": 1,
                            "DiskSize": 200,
                            "DiskType": "CLOUD_HSSD",
                            "InstanceType": "S6.2XLARGE32",
                            "LocalDiskNum": 0,
                            "MemSize": 32768,
                            "MultiDisks": [],
                            "RootSize": 70,
                            "Spec": "CVM.S6",
                            "StorageType": 6,
                            "Tags": null
                        },
                        "ResourceConfigId": 20560,
                        "UpdateTime": "2024-04-08 15:13:04"
                    }
                ],
                "ResourceType": "TASK"
            },
            {
                "ResourceData": [
                    {
                        "CreateTime": "2024-04-08 22:04:42",
                        "IsDefault": "DEFAULT",
                        "MaxResourceNum": 0,
                        "Resource": {
                            "Cpu": 4,
                            "DiskNum": 1,
                            "DiskSize": 200,
                            "DiskType": "CLOUD_HSSD",
                            "InstanceType": "SA2.LARGE8",
                            "LocalDiskNum": 0,
                            "MemSize": 8192,
                            "MultiDisks": [],
                            "RootSize": 70,
                            "Spec": "CVM.SA2",
                            "StorageType": 6,
                            "Tags": null
                        },
                        "ResourceConfigId": 20563,
                        "UpdateTime": "2024-04-08 22:04:42"
                    }
                ],
                "ResourceType": "ROUTER"
            }
        ],
        "RequestId": "638ef562-a954-4963-ae70-b54c2dd2bf94"
    }
}
```

