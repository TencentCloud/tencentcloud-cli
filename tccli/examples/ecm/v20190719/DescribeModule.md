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
        "RequestId": "5c266edc-86eb-416c-8425-1aeec3117760",
        "ModuleItemSet": [
            {
                "NodeInstanceNum": {
                    "NodeNum": 3,
                    "InstanceNum": 3
                },
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
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 1,
                    "InstanceNum": 1
                },
                "Module": {
                    "ModuleId": "em-w32agsp5",
                    "ModuleName": "test2",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 100,
                    "DefaultImage": {
                        "ImageId": "img-9qabwvbn",
                        "ImageName": "CentOS 7.6 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CentOS 7.6 64位",
                        "ImageDescription": "CentOS 7.6 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CentOS",
                        "OsVersion": "7.6.0",
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
                        "InstanceType": "SN3ne.LARGE8",
                        "Vcpu": 4,
                        "Memory": 8,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 50,
                    "CreateTime": "2020-03-09 11:08:13"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-m381mn2a",
                    "ModuleName": "element_24c48g",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 25,
                    "DefaultImage": {
                        "ImageId": "img-dkwyg6sr",
                        "ImageName": "CentOS 7.3 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CentOS 7.3 64位",
                        "ImageDescription": "CentOS 7.3 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CentOS",
                        "OsVersion": "7.3.0",
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
                        "InstanceType": "SN3ne.6XLARGE48",
                        "Vcpu": 24,
                        "Memory": 48,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-02-29 17:22:43"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-mmrhrfc1",
                    "ModuleName": "element_dpdk",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 35,
                    "DefaultImage": {
                        "ImageId": "img-bh86p0sv",
                        "ImageName": "Tencent Linux Release 2.2 (Final)",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "Tencent Linux Release 2.2 (Final)",
                        "ImageDescription": "Tencent Linux Release 2.2 (Final)",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "Tencent",
                        "OsVersion": "0.0.0",
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
                        "InstanceType": "SN3ne.SMALL2",
                        "Vcpu": 1,
                        "Memory": 2,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-02-13 23:47:06"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 1,
                    "InstanceNum": 1
                },
                "Module": {
                    "ModuleId": "em-317xx08p",
                    "ModuleName": "test3",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 534,
                    "DefaultImage": {
                        "ImageId": "img-9qabwvbn",
                        "ImageName": "CentOS 7.6 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CentOS 7.6 64位",
                        "ImageDescription": "CentOS 7.6 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CentOS",
                        "OsVersion": "7.6.0",
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
                    "DefaultDataDiskSize": 49,
                    "CreateTime": "2020-02-11 22:31:55"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-fkvxj45b",
                    "ModuleName": "ff-11",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 25,
                    "DefaultImage": {
                        "ImageId": "img-0hvei5hp",
                        "ImageName": "CoreOS 1745.5.0 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CoreOS 1745.5.0 64位",
                        "ImageDescription": "CoreOS 1745.5.0 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CoreOS",
                        "OsVersion": "1745.5.0",
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
                        "InstanceType": "SN3ne.SMALL2",
                        "Vcpu": 1,
                        "Memory": 2,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-01-19 19:30:02"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-j7fm12h7",
                    "ModuleName": "CENOS72",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 25,
                    "DefaultImage": {
                        "ImageId": "img-31tjrtph",
                        "ImageName": "CentOS 7.2 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CentOS 7.2 64位",
                        "ImageDescription": "CentOS 7.2 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CentOS",
                        "OsVersion": "7.2.0",
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
                        "InstanceType": "SN3ne.SMALL2",
                        "Vcpu": 1,
                        "Memory": 2,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-01-17 19:40:18"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-280u8ahy",
                    "ModuleName": "subao",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 25,
                    "DefaultImage": {
                        "ImageId": "img-pyqx34y1",
                        "ImageName": "Ubuntu Server 16.04.1 LTS 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "Ubuntu Server 16.04.1 LTS 64位",
                        "ImageDescription": "Ubuntu Server 16.04.1 LTS 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "Ubuntu",
                        "OsVersion": "16.4.1",
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
                        "InstanceType": "SN3ne.4XLARGE32",
                        "Vcpu": 16,
                        "Memory": 32,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-01-17 18:06:13"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-ywdwnyy4",
                    "ModuleName": "Ubuntu Test",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 25,
                    "DefaultImage": {
                        "ImageId": "img-pi0ii46r",
                        "ImageName": "Ubuntu Server 18.04.1 LTS 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "Ubuntu Server 18.04.1 LTS 64位",
                        "ImageDescription": "Ubuntu Server 18.04.1 LTS 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "Ubuntu",
                        "OsVersion": "18.4.1",
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
                        "InstanceType": "SN3ne.SMALL2",
                        "Vcpu": 1,
                        "Memory": 2,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 0,
                    "CreateTime": "2020-01-06 14:48:36"
                }
            },
            {
                "NodeInstanceNum": {
                    "NodeNum": 0,
                    "InstanceNum": 0
                },
                "Module": {
                    "ModuleId": "em-i4kpcfd6",
                    "ModuleName": "YTKYZ",
                    "ModuleState": "NORMAL",
                    "DefaultBandwidth": 5000,
                    "DefaultImage": {
                        "ImageId": "img-9qabwvbn",
                        "ImageName": "CentOS 7.6 64位",
                        "ImageState": "NORMAL",
                        "ImageType": "PUBLIC_IMAGE",
                        "ImageOwner": 0,
                        "ImageOsName": "CentOS 7.6 64位",
                        "ImageDescription": "CentOS 7.6 64位",
                        "Architecture": "x86_64",
                        "OsType": "linux",
                        "Platform": "CentOS",
                        "OsVersion": "7.6.0",
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
                        "InstanceType": "SN3ne.8XLARGE64",
                        "Vcpu": 32,
                        "Memory": 64,
                        "Frequency": "2.5 GHz",
                        "CpuModelName": "Intel Xeon Skylake 6133",
                        "ExtInfo": ""
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultDataDiskSize": 100,
                    "CreateTime": "2020-01-03 16:28:38"
                }
            }
        ],
        "TotalCount": 17
    }
}
```

