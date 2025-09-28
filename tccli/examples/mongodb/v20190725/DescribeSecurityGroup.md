**Example 1: 查询实例安全组**

查询当前实例已绑定的全部安全组

Input: 

```
tccli mongodb DescribeSecurityGroup --cli-unfold-argument  \
    --InstanceId cmgo-p8vn****
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2022-06-08 17:06:38",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "**.**.**.**/24",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "8086",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "**.**.**.**/24",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "****",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "**.**.**.**/24",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "****",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "**.**.**.**/24",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "****",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "**.**.**.**/24",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "****",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "ipm-pvcdf2ty",
                        "CidrIp": "",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "**,**,**,****,**,****",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-0klp****",
                "SecurityGroupName": "default",
                "SecurityGroupRemark": "System created security group"
            }
        ],
        "RequestId": "21d6a495-f46d-4440-bd25-d4e36f51afdd"
    }
}
```

