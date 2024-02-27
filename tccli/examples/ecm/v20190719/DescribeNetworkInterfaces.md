**Example 1: 查询弹性网卡列表**



Input: 

```
tccli ecm DescribeNetworkInterfaces --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "NetworkInterfaceSet": [
            {
                "NetworkInterfaceId": "eni-dqcedwp7",
                "NetworkInterfaceName": "TEST",
                "NetworkInterfaceDescription": "TEST",
                "SubnetId": "subnet-o6pv7si8",
                "VpcId": "vpc-j8s8351p",
                "GroupSet": [
                    "esg-fcx8o80o"
                ],
                "Primary": true,
                "MacAddress": "20:90:6F:34:59:4F",
                "State": "AVAILABLE",
                "PrivateIpAddressSet": [
                    {
                        "PrivateIpAddress": "11.171.73.41",
                        "Primary": true,
                        "PublicIpAddress": "60.28.209.138",
                        "AddressId": "",
                        "Description": "TEST",
                        "IsWanIpBlocked": true,
                        "State": "AVAILABLE"
                    }
                ],
                "Attachment": {
                    "InstanceId": "ein-05ihbvco",
                    "DeviceIndex": 1,
                    "InstanceAccountId": "1257940589",
                    "AttachTime": "2022-11-17 08:49:10"
                },
                "Zone": "ap-guangzhou-yunyou-cm-1",
                "CreatedTime": "2022-11-17 08:49:10",
                "Ipv6AddressSet": [
                    {
                        "Address": " 2409:8c50:a00:2035:0:9b58:a740:5945",
                        "Primary": true,
                        "AddressId": "",
                        "Description": "TEST",
                        "IsWanIpBlocked": true,
                        "State": "PENDING"
                    }
                ],
                "TagSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "EniType": 1,
                "EcmRegion": "ap-ningbo-ecm-ct2",
                "Business": "cvm"
            }
        ],
        "RequestId": "8f7fb33d-642f-43d7-bc8f-2d17efbfb49c"
    }
}
```

