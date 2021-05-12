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
        "Groups": [
            {
                "CreateTime": "2021-01-07 16:38:48",
                "Inbound": [
                    {
                        "Action": "DROP",
                        "CidrIp": "0.0.0.0/0",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "DROP",
                        "CidrIp": "::/0",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "DROP",
                        "CidrIp": "0.0.0.0/0",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "DROP",
                        "CidrIp": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "sg-7pw2qq97",
                "SecurityGroupName": "全拒绝",
                "SecurityGroupRemark": "暴露全部端口到公网和内网，有一定安全风险"
            }
        ],
        "RequestId": "b1886334-acfe-4445-8429-e11a6e7b3851"
    }
}
```

