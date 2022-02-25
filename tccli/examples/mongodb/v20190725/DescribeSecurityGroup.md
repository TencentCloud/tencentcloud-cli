**Example 1: 查询实例安全组**



Input: 

```
tccli mongodb DescribeSecurityGroup --cli-unfold-argument  \
    --InstanceId cmgo-p8vnipr5
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Groups": [
            {
                "Outbound": [
                    {
                        "PortRange": "xx",
                        "CidrIp": "xx",
                        "ServiceModule": "xx",
                        "AddressModule": "xx",
                        "Action": "xx",
                        "IpProtocol": "xx",
                        "Id": "xx",
                        "Desc": "xx"
                    },
                    {
                        "PortRange": "xx",
                        "CidrIp": "xx",
                        "Action": "xx",
                        "AddressModule": "xx",
                        "ServiceModule": "xx",
                        "IpProtocol": "xx",
                        "Id": "xx",
                        "Desc": "xx"
                    }
                ],
                "SecurityGroupName": "xx",
                "Inbound": [
                    {
                        "PortRange": "xx",
                        "CidrIp": "xx",
                        "ServiceModule": "xx",
                        "AddressModule": "xx",
                        "Action": "xx",
                        "IpProtocol": "xx",
                        "Id": "xx",
                        "Desc": "xx"
                    },
                    {
                        "PortRange": "xx",
                        "CidrIp": "xx",
                        "Action": "xx",
                        "AddressModule": "xx",
                        "ServiceModule": "xx",
                        "IpProtocol": "xx",
                        "Id": "xx",
                        "Desc": "xx"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "xx",
                "SecurityGroupRemark": "xx",
                "CreateTime": "xx"
            }
        ]
    }
}
```

