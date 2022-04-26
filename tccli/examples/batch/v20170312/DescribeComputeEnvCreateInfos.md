**Example 1: 查看计算环境创建信息列表**



Input: 

```
tccli batch DescribeComputeEnvCreateInfos --cli-unfold-argument  \
    --EnvIds env-lcx7qbbr
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "bb976df4-42a0-41cc-82d4-69bea1007083",
        "ComputeEnvCreateInfoSet": [
            {
                "EnvId": "env-lcx7qbbr",
                "Notifications": [
                    {
                        "EventConfigs": [
                            {
                                "EventName": "COMPUTE_ENV_CREATED_SUCCESS",
                                "EventVars": [
                                    {
                                        "Name": "COMPUTE_ENV_CREATED_SUCCESS",
                                        "Value": "COMPUTE_ENV_CREATED_SUCCESS"
                                    }
                                ]
                            }
                        ],
                        "TopicName": "compute-env-topic"
                    }
                ],
                "Tags": [
                    {
                        "Value": "test",
                        "Key": "test-env"
                    }
                ],
                "Authentications": [
                    {
                        "SecretKey": "xx",
                        "SecretId": "xx",
                        "Scene": "xx"
                    }
                ],
                "EnvData": {
                    "VirtualPrivateCloud": {
                        "SubnetId": "subnet-23syenxk",
                        "AsVpcGateway": true,
                        "Ipv6AddressCount": 1,
                        "VpcId": "vpc-1xnwrxw2",
                        "PrivateIpAddresses": [
                            "10.10.2.29"
                        ]
                    },
                    "LoginSettings": {
                        "Password": "xx",
                        "KeepImageLogin": "True",
                        "KeyIds": [
                            "xx"
                        ]
                    },
                    "InstanceMarketOptions": {
                        "SpotOptions": {
                            "SpotInstanceType": "one-time",
                            "MaxPrice": "1"
                        },
                        "MarketType": "spot"
                    },
                    "SystemDisk": {
                        "DiskSize": 0,
                        "CdcId": "xx",
                        "DiskId": "disk-sdfk23nw",
                        "DiskType": "CLOUD_SSD"
                    },
                    "InstanceTypes": [
                        "S5.SMALL2"
                    ],
                    "Zones": [
                        "ap-guangzhou-2"
                    ],
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "EnhancedService": {
                        "SecurityService": {
                            "Enabled": true
                        },
                        "MonitorService": {
                            "Enabled": true
                        },
                        "AutomationService": {
                            "Enabled": true
                        }
                    },
                    "SecurityGroupIds": [
                        "xx"
                    ],
                    "InternetAccessible": {
                        "PublicIpAssigned": true,
                        "InternetChargeType": "POSTPAID_BY_HOUR",
                        "BandwidthPackageId": "xx",
                        "InternetMaxBandwidthOut": 0
                    },
                    "VirtualPrivateClouds": [
                        {
                            "SubnetId": "subnet-23syenxk",
                            "AsVpcGateway": true,
                            "Ipv6AddressCount": 1,
                            "VpcId": "vpc-1xnwrxw2",
                            "PrivateIpAddresses": [
                                "10.10.2.29"
                            ]
                        }
                    ],
                    "ImageId": "img-3sdke3x2",
                    "InstanceName": "test-env",
                    "InstanceType": "S5.SMALL2",
                    "InstanceTypeOptions": {
                        "Memory": 1,
                        "CPU": 1,
                        "InstanceCategories": [
                            "ALL"
                        ]
                    },
                    "DataDisks": [
                        {
                            "DeleteWithInstance": true,
                            "Encrypt": true,
                            "CdcId": "xx",
                            "DiskType": "CLOUD_SSD",
                            "ThroughputPerformance": 0,
                            "KmsKeyId": "kms-213k73kx",
                            "DiskSize": 0,
                            "SnapshotId": "snap-fsdekxe2",
                            "DiskId": "xx"
                        }
                    ]
                },
                "EnvDescription": "test-env",
                "MountDataDisks": [
                    {
                        "FileSystemType": "ext4",
                        "LocalPath": "/mnt"
                    }
                ],
                "DesiredComputeNodeCount": 1,
                "EnvName": "test-env",
                "InputMappings": [
                    {
                        "SourcePath": "cos://test-1111123424.cos.ap-guangzhou.myqcloud.com/batchtest/input/",
                        "DestinationPath": "/opt/data",
                        "MountOptionParameter": ""
                    }
                ],
                "EnvType": "MANAGED"
            }
        ]
    }
}
```

