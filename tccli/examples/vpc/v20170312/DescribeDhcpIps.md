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
    --Filters.0.Values dhcpip-12345678
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
        "TotalCount": 1,
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

**Example 3: 根据DhcpIpIds查询DhcpIp列表**



Input: 

```
tccli vpc DescribeDhcpIps --cli-unfold-argument  \
    --DhcpIpIds dhcpip-12345678
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
        "TotalCount": 1,
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

