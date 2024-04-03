**Example 1: 查询实例安全组**

查询实例安全组

Input: 

```
tccli postgres DescribeDBInstanceSecurityGroups --cli-unfold-argument  \
    --DBInstanceId postgres-i2q4utnp
```

Output: 
```
{
    "Response": {
        "RequestId": "770234c2-8a51-4d06-b3f7-4454664848b1",
        "SecurityGroupSet": [
            {
                "CreateTime": "2022-10-20 21:38:20",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Ping服务",
                        "IpProtocol": "icmp",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Ping服务",
                        "IpProtocol": "icmpv6",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Linux SSH登录",
                        "IpProtocol": "tcp",
                        "PortRange": "22"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Linux SSH登录",
                        "IpProtocol": "tcp",
                        "PortRange": "22"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Windows远程登录",
                        "IpProtocol": "tcp",
                        "PortRange": "3389"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Windows远程登录",
                        "IpProtocol": "tcp",
                        "PortRange": "3389"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "10.0.0.0/8",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "172.16.0.0/12",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "192.168.0.0/16",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "80"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "80"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "443"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "443"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "",
                        "Description": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupDescription": "自定义模板",
                "SecurityGroupId": "sg-91jbmkp1",
                "SecurityGroupName": "自定义模板-20221020213819279"
            }
        ]
    }
}
```

**Example 2: 查询只读组安全组**

查询只读组安全组

Input: 

```
tccli postgres DescribeDBInstanceSecurityGroups --cli-unfold-argument  \
    --ReadOnlyGroupId pgrogrp-nqwpkjb
```

Output: 
```
{
    "Response": {
        "RequestId": "47e3764e-bce4-477a-a293-49ffa1bfb447",
        "SecurityGroupSet": [
            {
                "CreateTime": "2022-08-30 21:36:58",
                "Inbound": [],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupDescription": "自定义222",
                "SecurityGroupId": "sg-116auwb1",
                "SecurityGroupName": "自定义222-202208302136517989"
            },
            {
                "CreateTime": "2022-10-20 21:38:20",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Ping服务",
                        "IpProtocol": "icmp",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Ping服务",
                        "IpProtocol": "icmpv6",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Linux SSH登录",
                        "IpProtocol": "tcp",
                        "PortRange": "22"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Linux SSH登录",
                        "IpProtocol": "tcp",
                        "PortRange": "22"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Windows远程登录",
                        "IpProtocol": "tcp",
                        "PortRange": "3389"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Windows远程登录",
                        "IpProtocol": "tcp",
                        "PortRange": "3389"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "10.0.0.0/8",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "172.16.0.0/12",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "192.168.0.0/16",
                        "Description": "放通内网（云私有网络）",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "80"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "80"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "443"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "::/0",
                        "Description": "放通Web服务端口",
                        "IpProtocol": "tcp",
                        "PortRange": "443"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "",
                        "Description": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupDescription": "自定义模板",
                "SecurityGroupId": "sg-91jbmkp1",
                "SecurityGroupName": "自定义模板-20221020213819279"
            },
            {
                "CreateTime": "2022-08-22 17:34:08",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "一键放通入站规则",
                        "IpProtocol": "tcp",
                        "PortRange": "22,3389,80,443,20,21"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "一键放通入站规则",
                        "IpProtocol": "icmp",
                        "PortRange": "ALL"
                    }
                ],
                "Outbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Description": "一键放通出站规则",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupDescription": "拒绝所有",
                "SecurityGroupId": "sg-mpkb1net",
                "SecurityGroupName": "自定义-2022082217335427078"
            }
        ]
    }
}
```

