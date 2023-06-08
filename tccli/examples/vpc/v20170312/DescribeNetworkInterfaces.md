**Example 1: 查询弹性网卡列表**

查询弹性网卡列表

Input: 

```
tccli vpc DescribeNetworkInterfaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NetworkInterfaceSet": [
            {
                "MacAddress": "20:90:6F:F5:34:C7",
                "VpcId": "vpc-2kx9z6h3",
                "Business": "cvm",
                "Zone": "ap-guangzhou-2",
                "NetworkInterfaceId": "eni-f1xjkw1b",
                "Primary": false,
                "CdcId": "",
                "PrivateIpAddressSet": [
                    {
                        "Description": "",
                        "Primary": true,
                        "PrivateIpAddress": "192.168.0.13",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.0.15",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.0.17",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.0.24",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "NetworkInterfaceDescription": "aaa",
                "Ipv6AddressSet": [],
                "State": "AVAILABLE",
                "GroupSet": [
                    "sg-c2r7lnxh",
                    "sg-f9ekbxeq"
                ],
                "Attachment": {
                    "InstanceId": "ins-ymk3eje8",
                    "DeviceIndex": 1,
                    "InstanceAccountId": "251153169",
                    "AttachTime": "2021-01-08 16:36:49"
                },
                "TagSet": [],
                "EniType": 1,
                "CreatedTime": "2021-01-07 16:32:55",
                "SubnetId": "subnet-nao8lfro",
                "NetworkInterfaceName": "royhyangtest-main",
                "AttachType": 1
            }
        ],
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

**Example 2: 查询绑定了标签的网卡列表**

用tag:tag-key查询。

Input: 

```
tccli vpc DescribeNetworkInterfaces --cli-unfold-argument  \
    --Filters.0.Values TEST \
    --Filters.0.Name tag:Version
```

Output: 
```
{
    "Response": {
        "NetworkInterfaceSet": [
            {
                "VpcId": "vpc-709l0i0x",
                "SubnetId": "subnet-qymfizh2",
                "NetworkInterfaceId": "eni-p17uqigx",
                "NetworkInterfaceName": "test",
                "NetworkInterfaceDescription": "",
                "GroupSet": [
                    "sg-hcd8t9xj"
                ],
                "Primary": false,
                "MacAddress": "20:90:6F:FC:9F:69",
                "State": "AVAILABLE",
                "CreatedTime": "2018-04-18 21:46:56",
                "PrivateIpAddressSet": [
                    {
                        "Description": "12312",
                        "Primary": true,
                        "PrivateIpAddress": "192.168.3.10",
                        "AddressId": "",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.3.104",
                        "AddressId": "",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "13123",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.3.18",
                        "AddressId": "",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.3.223",
                        "AddressId": "",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    },
                    {
                        "Description": "",
                        "Primary": false,
                        "PrivateIpAddress": "192.168.3.86",
                        "AddressId": "",
                        "PublicIpAddress": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "Attachment": null,
                "Business": "cvm",
                "Zone": "ap-guangzhou-2",
                "Ipv6AddressSet": [
                    {
                        "Description": "",
                        "Primary": false,
                        "Address": "2402:4e00:1000:7400:0:9028:a2c9:85b2",
                        "AddressId": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "AttachType": 1,
                "EniType": 1,
                "CdcId": "",
                "TagSet": [
                    {
                        "Key": "Version",
                        "Value": "TEST"
                    },
                    {
                        "Key": "Compony",
                        "Value": "Compony-A"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "0c10340b-2551-4414-a8c7-8d90dc24ddd0"
    }
}
```

