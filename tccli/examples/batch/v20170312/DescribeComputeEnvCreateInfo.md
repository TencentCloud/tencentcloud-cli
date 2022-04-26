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
        "EnvId": "env-qleawxzt",
        "EnvType": "MANAGED",
        "DesiredComputeNodeCount": 2,
        "MountDataDisks": [
            {
                "FileSystemType": "xx",
                "LocalPath": "xx"
            }
        ],
        "EnvName": "test compute env",
        "EnvDescription": "test compute env",
        "InputMappings": [
            {
                "SourcePath": "cos://bucket-appid.cos.ap-hongkong.myqcloud.com/",
                "DestinationPath": "/mnt/disk/"
            },
            {
                "SourcePath": "cos://bucket-appid.cos.ap-hongkong.myqcloud.com/test/",
                "DestinationPath": "/mnt/input/"
            }
        ],
        "Notifications": [
            {
                "TopicName": "topic name",
                "EventConfigs": [
                    {
                        "EventName": "ComputeEnvCreated",
                        "EventVars": [
                            {
                                "Name": "name1",
                                "Value": "value1"
                            },
                            {
                                "Name": "name2",
                                "Value": "value2"
                            }
                        ]
                    }
                ]
            }
        ],
        "EnvData": {
            "VirtualPrivateCloud": {
                "SubnetId": "subnet-8axej2jc",
                "VpcId": "vpc-cg18la4l"
            },
            "SystemDisk": {
                "DiskSize": 50,
                "DiskType": "CLOUD_BASIC"
            },
            "InternetAccessible": {
                "PublicIpAssigned": "TRUE",
                "InternetMaxBandwidthOut": 50
            },
            "ImageId": "img-bd78fy2t",
            "InstanceType": "S1.SMALL2",
            "DataDisks": [
                {
                    "DiskSize": 50,
                    "DiskType": "CLOUD_BASIC"
                }
            ]
        },
        "Tags": [
            {
                "Key": "batch-test-tag-env-key",
                "Value": "batch-test-tag-env-value1"
            }
        ],
        "Authentications": [
            {
                "SecretKey": "xx",
                "SecretId": "xx",
                "Scene": "xx"
            }
        ],
        "RequestId": "578f3fae-6908-4521-ac07-17c2cffcd5ae"
    }
}
```

