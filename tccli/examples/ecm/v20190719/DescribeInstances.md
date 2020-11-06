**Example 1: 通过过滤条件获取实例信息**

通过指定过滤条件来获取实例的信息。

Input: 

```
tccli ecm DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "InstanceSet": [
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-bb0ab3pc",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-91p8tj1p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:13:51",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-5wrpefy1",
                    "ModuleName": "jiaxuan"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "3c3e605a-33a0-41ca-9251-5f115a531c3e",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.2XLARGE16",
                    "Vcpu": 8,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 16,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.6"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:13:51",
                "InstanceName": "jiaxuan滨海_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:13:51",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-m5gnw3tv",
                            "NetworkInterfaceName": "ein-bb0ab3pc Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.23",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 25,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.6"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.6"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.23",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 25,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            },
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-b6kee4dg",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-9tvkpn8p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:12:24",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-xgi6r1hk",
                    "ModuleName": "视频V8-cedricliu"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "edf97143-b1e3-43d9-b34b-cfcf3fba1820",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.4XLARGE32",
                    "Vcpu": 16,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 32,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.17"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:12:24",
                "InstanceName": "jiaxuan滨海机器_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:12:24",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-mhym6o89",
                            "NetworkInterfaceName": "ein-b6kee4dg Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.27",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 105,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.17"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.17"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.27",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 105,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            },
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-5uhtyyps",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-0fqlcnj7",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:12:24",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-xgi6r1hk",
                    "ModuleName": "视频V8-cedricliu"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "e85e02fb-8efd-4728-a3d7-10cf913ed4e5",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.4XLARGE32",
                    "Vcpu": 16,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 32,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.4"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:12:24",
                "InstanceName": "jiaxuan滨海机器_勿删1",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:12:24",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-i7nvrvbj",
                            "NetworkInterfaceName": "ein-5uhtyyps Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.39",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 105,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.4"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.4"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.39",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 105,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            }
        ],
        "TotalCount": 3
    }
}
```

**Example 2: 按照创建时间倒序查询最近的两个实例**



Input: 

```
tccli ecm DescribeInstances --cli-unfold-argument  \
    --OrderByField timestamp \
    --OrderDirection 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "InstanceSet": [
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-bb0ab3pc",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-91p8tj1p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:13:51",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-5wrpefy1",
                    "ModuleName": "jiaxuan"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "3c3e605a-33a0-41ca-9251-5f115a531c3e",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.2XLARGE16",
                    "Vcpu": 8,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 16,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.6"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:13:51",
                "InstanceName": "jiaxuan滨海_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:13:51",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-m5gnw3tv",
                            "NetworkInterfaceName": "ein-bb0ab3pc Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.23",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 25,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.6"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.6"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.23",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 25,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            },
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-b6kee4dg",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-9tvkpn8p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:12:24",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-xgi6r1hk",
                    "ModuleName": "视频V8-cedricliu"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "edf97143-b1e3-43d9-b34b-cfcf3fba1820",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.4XLARGE32",
                    "Vcpu": 16,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 32,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.17"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:12:24",
                "InstanceName": "jiaxuan滨海机器_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:12:24",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-mhym6o89",
                            "NetworkInterfaceName": "ein-b6kee4dg Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.27",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 105,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.17"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.17"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.27",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 105,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            }
        ],
        "TotalCount": 15
    }
}
```

**Example 3: 用vpc-id查询实例**



Input: 

```
tccli ecm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-ec3mnb4d
```

Output: 
```
{
    "Response": {
        "RequestId": "",
        "InstanceSet": [
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-bb0ab3pc",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-91p8tj1p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:13:51",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-5wrpefy1",
                    "ModuleName": "jiaxuan"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "3c3e605a-33a0-41ca-9251-5f115a531c3e",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.2XLARGE16",
                    "Vcpu": 8,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 16,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.6"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:13:51",
                "InstanceName": "jiaxuan滨海_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:13:51",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-m5gnw3tv",
                            "NetworkInterfaceName": "ein-bb0ab3pc Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.23",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 25,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.6"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.6"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.23",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 25,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            },
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-b6kee4dg",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-9tvkpn8p",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:12:24",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-xgi6r1hk",
                    "ModuleName": "视频V8-cedricliu"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "edf97143-b1e3-43d9-b34b-cfcf3fba1820",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.4XLARGE32",
                    "Vcpu": 16,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 32,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.17"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:12:24",
                "InstanceName": "jiaxuan滨海机器_勿删2",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:12:24",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-mhym6o89",
                            "NetworkInterfaceName": "ein-b6kee4dg Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.27",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 105,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.17"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.17"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.27",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 105,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            },
            {
                "DataDiskSize": 0,
                "RestrictState": "NORMAL",
                "InstanceId": "ein-5uhtyyps",
                "ISP": "CTCC",
                "SecurityGroupIds": [],
                "SystemDisk": {
                    "DiskType": "LOCAL_BASIC",
                    "DiskId": "ldisk-0fqlcnj7",
                    "DiskSize": 50
                },
                "ExpireTime": "2020-09-27 16:12:24",
                "TagSet": null,
                "SimpleModule": {
                    "ModuleId": "em-xgi6r1hk",
                    "ModuleName": "视频V8-cedricliu"
                },
                "DataDisks": null,
                "LatestOperationState": "SUCCESS",
                "UUID": "e85e02fb-8efd-4728-a3d7-10cf913ed4e5",
                "SystemDiskSize": 50,
                "InstanceTypeConfig": {
                    "Frequency": "2.5 GHz",
                    "InstanceType": "SN3ne.4XLARGE32",
                    "Vcpu": 16,
                    "InstanceFamilyConfig": {
                        "InstanceFamilyName": "标准型SN3ne",
                        "InstanceFamily": "SN3ne"
                    },
                    "InstanceFamilyTypeConfig": {
                        "InstanceFamilyTypeName": "标准型",
                        "InstanceFamilyType": "S"
                    },
                    "CpuModelName": "Intel Xeon Skylake 6133",
                    "Memory": 32,
                    "ExtInfo": ""
                },
                "RenewFlag": 0,
                "VirtualPrivateCloud": {
                    "PrivateIpAddresses": [
                        "10.11.12.4"
                    ],
                    "VpcId": "vpc-95ytv1vr",
                    "AsVpcGateway": false,
                    "SubnetId": "subnet-fua8fff8",
                    "Ipv6AddressCount": 0
                },
                "IsolatedTime": "2020-09-27 16:12:24",
                "InstanceName": "jiaxuan滨海机器_勿删1",
                "Position": {
                    "ZoneInfo": {
                        "ZoneId": 12000001,
                        "Zone": "ap-bhmini-ecm-1",
                        "ZoneName": "腾讯滨海专区"
                    },
                    "Country": {
                        "CountryName": "中国",
                        "CountryId": "china"
                    },
                    "Area": {
                        "AreaName": "华南",
                        "AreaId": "china-south"
                    },
                    "Province": {
                        "ProvinceId": "china-south-guangdong",
                        "ProvinceName": "广东"
                    },
                    "City": {
                        "CityName": "深圳",
                        "CityId": "china-south-guangdong-shenzhen"
                    },
                    "RegionInfo": {
                        "RegionId": 0,
                        "Region": "ap-bhmini-ecm",
                        "RegionName": "腾讯滨海专区"
                    }
                },
                "CreateTime": "2020-09-27 16:12:24",
                "Image": {
                    "SrcImage": {
                        "InstanceName": "",
                        "InstanceId": "",
                        "ImageOsName": "centos_test",
                        "ImageId": "img-test",
                        "ImageName": "centos",
                        "RegionID": 20,
                        "RegionName": "上海",
                        "ImageType": "",
                        "ImageDescription": "info_test",
                        "Region": "ap-shanghai"
                    },
                    "ImageOsName": "CentOS 7.6 64位",
                    "ImageId": "img-9qabwvbn",
                    "Platform": "CentOS",
                    "ImageName": "CentOS 7.6 64位",
                    "ImageCreateTime": "",
                    "ImageOwner": 0,
                    "ImageSource": "OFFICIAL",
                    "ImageType": "PUBLIC_IMAGE",
                    "OsType": "linux",
                    "OsVersion": "7.6.0",
                    "ImageState": "NORMAL",
                    "ImageDescription": "CentOS 7.6 64位",
                    "Architecture": "x86_64",
                    "ImageSize": 50
                },
                "InstanceState": "RUNNING",
                "Internet": {
                    "InstanceNetworkInfoSet": [
                        {
                            "Primary": true,
                            "NetworkInterfaceId": "eni-i7nvrvbj",
                            "NetworkInterfaceName": "ein-5uhtyyps Primary ENI",
                            "AddressInfoSet": [
                                {
                                    "PublicIPAddressInfo": {
                                        "PublicIPAddress": "118.126.126.39",
                                        "ISP": {
                                            "ISPName": "电信",
                                            "ISPId": "CTCC"
                                        },
                                        "MaxBandwidthOut": 105,
                                        "ChargeMode": "BANDWIDTH_PACKAGE",
                                        "MaxBandwidthIn": 0
                                    },
                                    "PrivateIPAddressInfo": {
                                        "PrivateIPAddress": "10.11.12.4"
                                    }
                                }
                            ]
                        }
                    ],
                    "PrivateIPAddressSet": [
                        {
                            "PrivateIPAddress": "10.11.12.4"
                        }
                    ],
                    "PublicIPAddressSet": [
                        {
                            "PublicIPAddress": "118.126.126.39",
                            "ISP": {
                                "ISPName": "电信",
                                "ISPId": "CTCC"
                            },
                            "MaxBandwidthOut": 105,
                            "ChargeMode": "BANDWIDTH_PACKAGE",
                            "MaxBandwidthIn": 0
                        }
                    ]
                },
                "NewFlag": 0,
                "ExpireState": "NORMAL",
                "PayMode": 0,
                "LatestOperation": "ResetInstancesPassword"
            }
        ],
        "TotalCount": 12
    }
}
```

