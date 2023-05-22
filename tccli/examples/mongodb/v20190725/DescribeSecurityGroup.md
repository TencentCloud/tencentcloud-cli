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
                "ProjectId": 0,
                "CreateTime": "2022-03-23 12:05:22",
                "Inbound": [
                    {
                        "Action": "Describe*",
                        "CidrIp": "127.0.0.1",
                        "PortRange": "27017",
                        "IpProtocol": "tcp",
                        "Id": "abc",
                        "AddressModule": "",
                        "ServiceModule": "",
                        "Desc": "localip"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "Describe*",
                        "CidrIp": "127.0.0.1",
                        "PortRange": "27017",
                        "IpProtocol": "tcp",
                        "Id": "abc",
                        "AddressModule": "",
                        "ServiceModule": "",
                        "Desc": "localip"
                    }
                ],
                "SecurityGroupId": "sg-cadead",
                "SecurityGroupName": "sg",
                "SecurityGroupRemark": "sg-mark"
            }
        ],
        "RequestId": "bc59fa05-d429-4bcf-863f-1f6f99295485"
    }
}
```

