**Example 1: 查看模块列表**

查看模块列表

Input: 

```
tccli ecm DescribeModule --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ModuleItemSet": [
            {
                "Module": {
                    "CloseIpDirect": 0,
                    "CreateTime": "2024-01-25 19:35:00",
                    "DataDisks": [
                        {
                            "DiskSize": 0,
                            "DiskType": "LOCAL_BASIC"
                        }
                    ],
                    "DefaultBandwidth": 1024,
                    "DefaultBandwidthIn": 1024,
                    "DefaultDataDiskSize": 0,
                    "DefaultImage": {
                        "Architecture": "x86_64",
                        "ImageCreateTime": "2024-01-24 19:21:08",
                        "ImageDescription": "t1版本测试",
                        "ImageId": "img-im4w1234",
                        "ImageName": "d-v21-new",
                        "ImageOsName": "Ubuntu 16.0 64位",
                        "ImageOwner": 123456,
                        "ImageSize": 50,
                        "ImageSource": "EXTERNAL_IMPORT",
                        "ImageState": "NORMAL",
                        "ImageType": "PRIVATE_IMAGE",
                        "IsSupportCloudInit": true,
                        "OsType": "linux",
                        "OsVersion": "16.0",
                        "Platform": "Ubuntu",
                        "SrcImage": {
                            "ImageDescription": "",
                            "ImageId": "img-im4s1234",
                            "ImageName": "tsImg",
                            "ImageOsName": "Ubuntu 16.0 64位",
                            "ImageType": "PRIVATE_IMAGE",
                            "InstanceId": "ein-123345",
                            "InstanceName": "ts",
                            "Region": "gz",
                            "RegionID": 0,
                            "RegionName": ""
                        },
                        "TaskId": "3281"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DisableWanIp": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": "",
                        "Frequency": "2.5 GHz",
                        "GpuModelName": null,
                        "InstanceFamilyConfig": {
                            "InstanceFamily": "S5",
                            "InstanceFamilyName": "标准型S5"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "S",
                            "InstanceFamilyTypeName": "标准型"
                        },
                        "InstanceType": "S5.2XLARGE16",
                        "Memory": 16,
                        "Vcpu": 8,
                        "Vgpu": null
                    },
                    "ModuleId": "em-n2e2345",
                    "ModuleName": "t1_u22",
                    "ModuleState": "NORMAL",
                    "SecurityGroupIds": [
                        "esg-g4k23455"
                    ],
                    "SystemDisk": {
                        "DiskId": "ldisk-1ly4f53h",
                        "DiskSize": 50,
                        "DiskType": "LOCAL_BASIC"
                    },
                    "TagSet": null,
                    "UserData": ""
                },
                "NodeInstanceNum": {
                    "InstanceNum": 8,
                    "NodeNum": 3
                }
            }
        ],
        "RequestId": "565a466c-cb44-4fd1-bbff-92f88986ab56",
        "TotalCount": 87
    }
}
```

