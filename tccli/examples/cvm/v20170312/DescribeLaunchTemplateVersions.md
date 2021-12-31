**Example 1: 查询实例模板版本信息**



Input: 

```
tccli cvm DescribeLaunchTemplateVersions --cli-unfold-argument  \
    --LaunchTemplateId lt-b8v1kcyq
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LaunchTemplateVersionSet": [
            {
                "LaunchTemplateVersion": 1,
                "LaunchTemplateVersionData": {
                    "VirtualPrivateCloud": {
                        "SubnetId": "subnet-he88kvqu",
                        "AsVpcGateway": false,
                        "Ipv6AddressCount": 0,
                        "VpcId": "vpc-dcteo7jd"
                    },
                    "InstanceCount": 1,
                    "Placement": {
                        "ProjectId": 0,
                        "Zone": "ap-guangzhou-2"
                    },
                    "SystemDisk": {
                        "DiskSize": 50,
                        "DiskType": "CLOUD_PREMIUM"
                    },
                    "ImageId": "img-8toqc6s3",
                    "InstanceChargeType": "POSTPAID_BY_HOUR",
                    "EnhancedService": {
                        "SecurityService": {
                            "Enabled": true
                        },
                        "MonitorService": {
                            "Enabled": true
                        }
                    },
                    "SecurityGroupIds": [
                        "sg-rf6ogz49"
                    ],
                    "InternetAccessible": {
                        "PublicIpAssigned": true,
                        "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
                        "InternetMaxBandwidthOut": 100
                    },
                    "InstanceName": "lt_test",
                    "InstanceType": "S1.SMALL2",
                    "DataDisks": [
                        {
                            "Encrypt": false,
                            "DeleteWithInstance": true,
                            "KmsKeyId": "",
                            "DiskSize": 50,
                            "DiskType": "CLOUD_PREMIUM"
                        },
                        {
                            "Encrypt": true,
                            "DeleteWithInstance": true,
                            "KmsKeyId": "",
                            "DiskSize": 60,
                            "DiskType": "CLOUD_PREMIUM"
                        }
                    ]
                },
                "CreationTime": "2020-12-17T01:54:31Z",
                "LaunchTemplateId": "lt-b8v1kcyq",
                "IsDefaultVersion": true,
                "LaunchTemplateVersionDescription": "",
                "CreatedBy": "251009920"
            }
        ],
        "RequestId": "b2da6ace-add1-48dc-ae73-6fc1eed95f1d"
    }
}
```

