**Example 1: 创建弹性网卡**



Input: 

```
tccli ecm CreateNetworkInterface --cli-unfold-argument  \
    --VpcId vpc-1111111 \
    --SubnetId subnet-22222222 \
    --NetworkInterfaceName Test \
    --NetworkInterfaceDescription Test \
    --EcmRegion ap-hangzhou-ecm
```

Output: 
```
{
    "Response": {
        "NetworkInterface": {
            "NetworkInterfaceId": "eni-12121212",
            "VpcId": "vpc-1111111",
            "SubnetId": "subnet-22222222",
            "NetworkInterfaceName": "Test",
            "NetworkInterfaceDescription": "Test",
            "MacAddress": "20:90:6F:62:33:E2",
            "PrivateIpAddressSet": [
                {
                    "PrivateIpAddress": "172.16.64.13",
                    "Primary": true,
                    "AddressId": "",
                    "PublicIpAddress": "",
                    "Description": "",
                    "IsWanIpBlocked": false,
                    "State": "PENDING"
                }
            ],
            "Attachment": null,
            "GroupSet": [],
            "Primary": false,
            "State": "PENDING",
            "Zone": "ap-hangzhou-ecm-1",
            "CreatedTime": "",
            "Ipv6AddressSet": [],
            "EcmRegion": "ap-hangzhou-ecm",
            "EniType": 0,
            "TagSet": []
        },
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

