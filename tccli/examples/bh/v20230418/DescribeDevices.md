**Example 1: 查询资产列表**

查询资产列表

Input: 

```
tccli bh DescribeDevices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DeviceSet": [
            {
                "Id": 1,
                "InstanceId": "ins-bhtest",
                "Name": "test-name",
                "PublicIp": "10.10.10.10",
                "PrivateIp": "127.0.0.1",
                "ApCode": "ap-guangzhou",
                "OsName": "Linux",
                "Kind": 1,
                "Port": 1,
                "GroupSet": [
                    {
                        "Id": 1,
                        "Name": "test-group-name",
                        "Department": {
                            "Id": "1",
                            "Name": "1",
                            "Managers": [
                                "1"
                            ],
                            "ManagerUsers": [
                                {
                                    "ManagerId": "1",
                                    "ManagerName": "test-name"
                                }
                            ]
                        },
                        "Count": 1
                    }
                ],
                "AccountCount": 1,
                "VpcId": "vpc-bhtest",
                "SubnetId": "subnet-bhtest",
                "Resource": {
                    "ResourceId": "bh-saas-test",
                    "ApCode": "ap-guangzhou",
                    "SvArgs": "sv_cds_dasb_saas_standard_50node",
                    "VpcId": "vpc-bhtest",
                    "Nodes": 1,
                    "RenewFlag": 1,
                    "ExpireTime": "2020-09-22T00:00:00+00:00",
                    "Status": 1,
                    "ResourceName": "test-name",
                    "Pid": 1,
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "ProductCode": "code",
                    "SubProductCode": "code",
                    "Zone": "ap-guangzhou-1",
                    "Expired": true,
                    "Deployed": true,
                    "VpcName": "vpc-name",
                    "VpcCidrBlock": "192.168.11.0/24",
                    "SubnetId": "subnet-bhtest",
                    "SubnetName": "test-name",
                    "CidrBlock": "192.168.11.0/24",
                    "PublicIpSet": [
                        "10.10.10.10"
                    ],
                    "PrivateIpSet": [
                        "192.168.0.1"
                    ],
                    "ModuleSet": [
                        "module1"
                    ],
                    "UsedNodes": 1,
                    "ExtendPoints": 1,
                    "PackageBandwidth": 1,
                    "PackageNode": 1,
                    "LogDeliveryArgs": "LogDeliveryArgsTest",
                    "LogDelivery": "LogDeliveryTest"
                },
                "Department": {
                    "Id": "1",
                    "Name": "1",
                    "Managers": [
                        "1"
                    ],
                    "ManagerUsers": [
                        {
                            "ManagerId": "1",
                            "ManagerName": "1"
                        }
                    ]
                },
                "IpPortSet": [
                    "127.0.0.1:20"
                ]
            }
        ],
        "RequestId": "ec7676f4-a498-4ef5-ad68-6678b16e45d7"
    }
}
```

**Example 2: 根据用户查询有访问权限的资产**

根据用户查询有访问权限的资产

Input: 

```
tccli bh DescribeDevices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DeviceSet": [
            {
                "AccountCount": 0,
                "ApCode": "ap-guangzhou",
                "ApName": "华南地区(广州)",
                "CloudAccountId": 6,
                "CloudAccountName": "DBImport",
                "Department": {
                    "Id": "1",
                    "Name": "腾讯云"
                },
                "DomainId": "",
                "DomainName": "",
                "EnableSSL": 0,
                "GroupSet": [],
                "IOAId": 0,
                "Id": 16851272,
                "InstanceId": "crs-gkkcxuzz",
                "IpPortSet": [
                    "10.0.0.71:6379"
                ],
                "Kind": 11,
                "ManageDimension": 1,
                "Name": "SSM_Redis_集群版",
                "OsName": "Redis",
                "OwnerAccountName": "堡垒机内部测试账号",
                "OwnerAccountUin": "100018268486",
                "OwnerAppId": 1305350016,
                "Port": 6379,
                "PrivateIp": "10.0.0.71",
                "ProviderName": "",
                "ProviderType": 1,
                "PublicIp": "",
                "SSLCertName": "",
                "SubnetId": "subnet-0q6ile8u",
                "SyncCloudDeviceStatus": 1,
                "SyncPodCount": 0,
                "TotalPodCount": 0,
                "VpcId": "vpc-ja90l5rb"
            }
        ],
        "TotalCount": 7508,
        "RequestId": "a48afc8d-cd74-4a06-ac57-3fd21646df63"
    }
}
```

