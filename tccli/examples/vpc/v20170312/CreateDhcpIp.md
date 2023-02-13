**Example 1: 创建DhcpIp**

创建DhcpIp

Input: 

```
tccli vpc CreateDhcpIp --cli-unfold-argument  \
    --SubnetId subnet-12345678 \
    --VpcId vpc-12345678 \
    --DhcpIpName test \
    --SecondaryPrivateIpAddressCount 1
```

Output: 
```
{
    "Response": {
        "DhcpIpSet": [
            {
                "DhcpIpId": "dhcpip-12345678",
                "DhcpIpName": "test",
                "PrivateIpAddress": "10.0.0.13",
                "VpcId": "vpc-12345678",
                "SubnetId": "subnet-12345678",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "State": "UNBIND",
                "CreatedTime": "2018-10-10 17:03:09"
            }
        ],
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

