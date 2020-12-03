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
        "TotalCount": 17,
        "ModuleItemSet": [
            {
                "NodeInstanceNum": {
                    "InstanceNum": 3,
                    "NodeNum": 3
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 48,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 8,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 16,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "RegionName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "ImageOsName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "ImageSource": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "OsVersion": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 106,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 1,
                    "NodeNum": 1
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 50,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 4,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 8,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 100,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 24,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 48,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 25,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 1,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 2,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 35,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 1,
                    "NodeNum": 1
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 49,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 8,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 16,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 534,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 1,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 2,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 25,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 1,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 2,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 25,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 16,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 32,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 25,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 0,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 1,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 2,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 25,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            },
            {
                "NodeInstanceNum": {
                    "InstanceNum": 0,
                    "NodeNum": 0
                },
                "Module": {
                    "ModuleName": "xx",
                    "DefaultDataDiskSize": 100,
                    "DefaultBandwidthIn": 0,
                    "InstanceTypeConfig": {
                        "CpuModelName": "xx",
                        "Vcpu": 32,
                        "InstanceFamilyConfig": {
                            "InstanceFamilyName": "xx",
                            "InstanceFamily": "xx"
                        },
                        "InstanceFamilyTypeConfig": {
                            "InstanceFamilyType": "xx",
                            "InstanceFamilyTypeName": "xx"
                        },
                        "Memory": 64,
                        "ExtInfo": "xx",
                        "Frequency": "xx",
                        "InstanceType": "xx"
                    },
                    "DefaultImage": {
                        "SrcImage": {
                            "ImageDescription": "xx",
                            "InstanceId": "xx",
                            "Region": "xx",
                            "RegionID": 0,
                            "ImageId": "xx",
                            "ImageName": "xx",
                            "ImageOsName": "xx",
                            "InstanceName": "xx",
                            "ImageType": "xx",
                            "RegionName": "xx"
                        },
                        "ImageCreateTime": "xx",
                        "ImageSize": 50,
                        "OsVersion": "xx",
                        "ImageDescription": "xx",
                        "ImageOwner": 0,
                        "ImageId": "xx",
                        "ImageState": "xx",
                        "Platform": "xx",
                        "ImageName": "xx",
                        "Architecture": "xx",
                        "OsType": "xx",
                        "ImageSource": "xx",
                        "ImageType": "xx",
                        "ImageOsName": "xx"
                    },
                    "DefaultSystemDiskSize": 50,
                    "DefaultBandwidth": 5000,
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "TagSet": [
                        {
                            "Key": "xx",
                            "Value": "xx"
                        }
                    ],
                    "CloseIpDirect": 0,
                    "ModuleState": "xx",
                    "CreateTime": "xx",
                    "ModuleId": "xx"
                }
            }
        ],
        "RequestId": "xx"
    }
}
```

