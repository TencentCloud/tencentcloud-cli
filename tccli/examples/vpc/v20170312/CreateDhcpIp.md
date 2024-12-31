**Example 1: 创建DhcpIp**

创建DhcpIp

Input: 

```
tccli vpc CreateDhcpIp --cli-unfold-argument  \
    --SubnetId subnet-6zwa44xm \
    --VpcId vpc-4tw1bxlq \
    --DhcpIpName demo \
    --SecondaryPrivateIpAddressCount 1
```

Output: 
```
{
    "Response": {
        "DhcpIpSet": [
            {
                "DhcpIpId": "dhcpip-ms7c7gcr",
                "DhcpIpName": "demo",
                "PrivateIpAddress": "10.0.0.13",
                "VpcId": "vpc-4tw1bxlq",
                "SubnetId": "subnet-6zwa44xm",
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

