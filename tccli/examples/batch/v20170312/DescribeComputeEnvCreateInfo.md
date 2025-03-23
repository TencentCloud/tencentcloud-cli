**Example 1: 查看计算环境的创建信息**



Input: 

```
tccli batch DescribeComputeEnvCreateInfo --cli-unfold-argument  \
    --EnvId env-lcpcej85
```

Output: 
```
{
    "Response": {
        "RequestId": "578f3fae-6908-4521-ac07-17c2cffcd5ae",
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
                "Value": "demo-tag",
                "Key": "demo-env1"
            }
        ],
        "Authentications": [
            {
                "SecretKey": "AKIDUdi1************9ThAzpuXIjNx",
                "SecretId": "Udi16***********Q9ThAzpuXIjN",
                "Scene": "COS"
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
                "Password": "Aa12**5678",
                "KeepImageLogin": "True",
                "KeyIds": [
                    "Qa123"
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
                "CdcId": "1",
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
                "sg-1234t1"
            ],
            "InternetAccessible": {
                "PublicIpAssigned": true,
                "InternetChargeType": "POSTPAID_BY_HOUR",
                "BandwidthPackageId": "dcaew",
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
                    "CdcId": "2",
                    "DiskType": "CLOUD_SSD",
                    "ThroughputPerformance": 0,
                    "KmsKeyId": "kms-213k73kx",
                    "DiskSize": 0,
                    "SnapshotId": "snap-fsdekxe2",
                    "DiskId": "disk-ecqwbck"
                }
            ]
        },
        "EnvDescription": "test-env",
        "MountDataDisks": [
            {
                "FileSystemType": "EXT4",
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
}
```

