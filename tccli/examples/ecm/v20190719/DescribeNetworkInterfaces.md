**Example 1: 查询弹性网卡列表**



Input: 

```
tccli ecm DescribeNetworkInterfaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetworkInterfaceSet": [
            {
                "NetworkInterfaceId": "eni-n1s3wvux",
                "NetworkInterfaceName": "字符串",
                "NetworkInterfaceDescription": "字符串",
                "SubnetId": "subnet-0790w1hs",
                "VpcId": "vpc-f3khnq0z",
                "GroupSet": [],
                "Primary": false,
                "MacAddress": "20:90:6F:6D:D9:B9",
                "State": "AVAILABLE",
                "PrivateIpAddressSet": [
                    {
                        "PrivateIpAddress": "10.0.0.8",
                        "Primary": true,
                        "PublicIpAddress": "",
                        "AddressId": "",
                        "Description": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "Attachment": null,
                "Zone": "ap-hangzhou-ecm-1",
                "EcmRegion": "ap-hangzhou-ecm",
                "CreatedTime": "2020-08-20 15:26:42",
                "Ipv6AddressSet": [],
                "TagSet": [],
                "EniType": 0
            },
            {
                "NetworkInterfaceId": "eni-f1xjkw1b",
                "NetworkInterfaceName": "安全组测试网卡",
                "NetworkInterfaceDescription": "安全组测试网卡描述",
                "SubnetId": "subnet-0790w1hs",
                "VpcId": "vpc-f3khnq0z",
                "GroupSet": [],
                "Primary": false,
                "MacAddress": "20:90:6F:69:1E:03",
                "State": "AVAILABLE",
                "PrivateIpAddressSet": [
                    {
                        "PrivateIpAddress": "10.0.0.16",
                        "Primary": true,
                        "PublicIpAddress": "",
                        "AddressId": "",
                        "Description": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "Attachment": null,
                "Zone": "ap-hangzhou-ecm-1",
                "EcmRegion": "ap-hangzhou-ecm",
                "CreatedTime": "2020-08-20 16:02:14",
                "Ipv6AddressSet": [],
                "TagSet": [],
                "EniType": 0
            },
            {
                "NetworkInterfaceId": "eni-rb7kjij1",
                "NetworkInterfaceName": "安全组测试网卡",
                "NetworkInterfaceDescription": "安全组测试网卡描述",
                "SubnetId": "subnet-5gnb2gls",
                "VpcId": "vpc-mbnu07m1",
                "GroupSet": [],
                "Primary": false,
                "MacAddress": "20:90:6F:90:0C:EF",
                "State": "AVAILABLE",
                "PrivateIpAddressSet": [
                    {
                        "PrivateIpAddress": "10.0.0.9",
                        "Primary": true,
                        "PublicIpAddress": "",
                        "AddressId": "",
                        "Description": "",
                        "IsWanIpBlocked": false,
                        "State": "AVAILABLE"
                    }
                ],
                "Attachment": null,
                "Zone": "ap-qingdao-ecm-1",
                "EcmRegion": "ap-qingdao-ecm",
                "CreatedTime": "2020-09-08 10:58:51",
                "Ipv6AddressSet": [],
                "TagSet": [],
                "EniType": 0
            }
        ],
        "TotalCount": 3,
        "RequestId": "8f7fb33d-642f-43d7-bc8f-2d17efbfb49c"
    }
}
```

