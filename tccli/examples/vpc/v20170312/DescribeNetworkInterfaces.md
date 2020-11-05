**Example 1: Querying the ENI list**



Input: 

```
tccli vpc DescribeNetworkInterfaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetworkInterfaceSet": [
            {
                "VpcId": "vpc-mrzkofih",
                "SubnetId": "subnet-nao8lfro",
                "NetworkInterfaceId": "eni-f1xjkw1b",
                "NetworkInterfaceName": "royhyangtest-main",
                "NetworkInterfaceDescription": "",
                "GroupSet": [
                    "sg-c2r7lnxh",
                    "sg-f9ekbxeq"
                ],
                "Primary": false,
                "MacAddress": "20: 90: 6F: F3: 3D: BD",
                "State": "AVAILABLE",
                "CreatedTime": "2017-11-16 19:56:00",
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
                "Attachment": {},
                "Zone": "ap-guangzhou-2"
            }
        ],
        "TotalCount": 1,
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

**Example 2: Querying the list of ENIs bound to the tag**

Make queries using tag:tag-key.

Input: 

```
tccli vpc DescribeNetworkInterfaces --cli-unfold-argument  \
    --Filters.0.Name tag:Version\
    --Filters.0.Values TEST
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

