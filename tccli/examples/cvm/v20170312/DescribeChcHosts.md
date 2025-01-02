**Example 1: 查看CHC物理服务器实例**

根据CHC物理服务器ID查看实例

Input: 

```
tccli cvm DescribeChcHosts --cli-unfold-argument  \
    --ChcIds chc-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "ChcHostSet": [
            {
                "BmcIp": "10.0.0.17",
                "BmcMAC": "52:54:00:71:B5:A1",
                "BmcSecurityGroupIds": [
                    "sg-8l03md6z"
                ],
                "BmcVirtualPrivateCloud": {
                    "SubnetId": "subnet-hmpeps7u",
                    "VpcId": "vpc-b9y7wgix",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 0,
                    "PrivateIpAddresses": [
                        "10.10.2.4"
                    ]
                },
                "CPU": 64,
                "ChcId": "chc-1a2b3c4d",
                "ChcInstanceFamily": "CHCS5",
                "ChcInstanceFamilyName": "高性能计算型CHCS5",
                "ChcInstanceType": "CHCS5.128C384M",
                "CreatedTime": "2024-07-19 16:41:20",
                "CvmInstanceId": "",
                "DeployExtraConfig": {
                    "BootFile": "pxelinux.0",
                    "BootType": "x86_uefi",
                    "MiniOsType": "public",
                    "NextServerAddress": "169.254.68.10"
                },
                "DeployIp": "172.16.0.17",
                "DeployMAC": "52:54:00:41:8D:7B",
                "DeploySecurityGroupIds": [
                    "sg-8l03md6z"
                ],
                "DeployVirtualPrivateCloud": {
                    "SubnetId": "subnet-pad8nabc",
                    "VpcId": "vpc-gbgzjb6r",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 0,
                    "PrivateIpAddresses": [
                        "10.10.2.4"
                    ]
                },
                "DeviceType": "CHCS5",
                "Disk": "480GB*2/3.84TB*12",
                "Gpu": "",
                "HardwareDescription": "64核 256GB 480GB*2/3.84TB*12",
                "InstanceName": "vlan502",
                "InstanceState": "PREPARED",
                "IsPredefinedType": true,
                "Memory": 256,
                "NetworkCard": "",
                "Placement": {
                    "Zone": "ap-guangzhou-2",
                    "ProjectId": 0
                },
                "ResaleAccountId": "",
                "ResaleAppId": "",
                "SaleStatus": "NOT_FOR_SALE",
                "SerialNumber": "7DF112345678",
                "Tags": [
                    {
                        "Key": "myKey",
                        "Value": "myValue"
                    }
                ],
                "TenantType": "HOSTING"
            }
        ],
        "RequestId": "d2ab63c0-576f-44c4-b6c1-f519fb58654b",
        "TotalCount": 1
    }
}
```

