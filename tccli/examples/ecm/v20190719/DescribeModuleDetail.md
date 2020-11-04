**Example 1: 查看模块详情**

查看模块详情

Input: 

```
tccli ecm DescribeModuleDetail --cli-unfold-argument  \
    --ModuleId em-eedttqfb
```

Output: 
```
{
    "Response": {
        "RequestId": "187c16d5-1f53-4e88-b684-077f0c7369b2",
        "Module": {
            "ModuleId": "em-eedttqfb",
            "ModuleName": "test1",
            "ModuleState": "NORMAL",
            "DefaultBandwidth": 106,
            "DefaultImage": {
                "ImageId": "img-oikl1tzv",
                "ImageName": "CentOS 7.5 64位",
                "ImageState": "NORMAL",
                "ImageType": "PUBLIC_IMAGE",
                "ImageOwner": 0,
                "ImageOsName": "CentOS 7.5 64位",
                "ImageDescription": "CentOS 7.5 64位",
                "Architecture": "x86_64",
                "OsType": "linux",
                "Platform": "CentOS",
                "OsVersion": "7.5.0",
                "ImageCreateTime": "",
                "ImageSize": 50
            },
            "InstanceTypeConfig": {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.2XLARGE16",
                "Vcpu": 8,
                "Memory": 16,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            "DefaultSystemDiskSize": 50,
            "DefaultDataDiskSize": 48,
            "CreateTime": "2020-03-09 17:03:44"
        },
        "ModuleCounter": {
            "ISPCounterSet": [
                {
                    "ProviderName": "CTCC",
                    "ProviderNodeNum": 1,
                    "ProvederInstanceNum": 1,
                    "ZoneInstanceInfoSet": [
                        {
                            "ZoneName": "北京三区（电信）",
                            "InstanceNum": 1
                        }
                    ]
                },
                {
                    "ProviderName": "CMCC",
                    "ProviderNodeNum": 2,
                    "ProvederInstanceNum": 2,
                    "ZoneInstanceInfoSet": [
                        {
                            "ZoneName": "北京一区（移动）",
                            "InstanceNum": 1
                        },
                        {
                            "ZoneName": "成都二区（移动）",
                            "InstanceNum": 1
                        }
                    ]
                }
            ],
            "NodeNum": 3,
            "InstanceNum": 3,
            "ProvinceNum": 2,
            "CityNum": 2
        }
    }
}
```

