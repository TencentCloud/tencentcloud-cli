**Example 1: 查询DhcpIp列表**



Input: 

```
tccli vpc DescribeDhcpIps --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DhcpIpSet": [
            {
                "DhcpIpId": "dhcpip-pxir56ns",
                "DhcpIpName": "demo",
                "PrivateIpAddress": "10.0.0.13",
                "VpcId": "vpc-n0yejvje",
                "SubnetId": "subnet-hj3he929",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "State": "UNBIND",
                "CreatedTime": "2018-10-10 17:03:09"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

**Example 2: 根据Filters查询DhcpIp列表**



Input: 

```
tccli vpc DescribeDhcpIps --cli-unfold-argument  \
    --Filters.0.Name dhcpip-id \
    --Filters.0.Values dhcpip-pxir56ns
```

Output: 
```
{
    "Response": {
        "DhcpIpSet": [
            {
                "DhcpIpId": "dhcpip-pxir56ns",
                "DhcpIpName": "demo",
                "PrivateIpAddress": "10.0.0.13",
                "VpcId": "vpc-n0yejvje",
                "SubnetId": "subnet-hj3he929",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "State": "UNBIND",
                "CreatedTime": "2018-10-10 17:03:09"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

**Example 3: 根据DhcpIpIds查询DhcpIp列表**



Input: 

```
tccli vpc DescribeDhcpIps --cli-unfold-argument  \
    --DhcpIpIds dhcpip-pxir56ns
```

Output: 
```
{
    "Response": {
        "DhcpIpSet": [
            {
                "DhcpIpId": "dhcpip-pxir56ns",
                "DhcpIpName": "demo",
                "PrivateIpAddress": "10.0.0.13",
                "VpcId": "vpc-n0yejvje",
                "SubnetId": "subnet-hj3he929",
                "NetworkInterfaceId": "",
                "InstanceId": "",
                "AddressIp": "",
                "State": "UNBIND",
                "CreatedTime": "2018-10-10 17:03:09"
            }
        ],
        "TotalCount": 1,
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

