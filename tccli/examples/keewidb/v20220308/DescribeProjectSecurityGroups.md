**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 0 \
    --Product keewidb \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2021-10-30 16:11:08",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "10.0.0.0/8",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "7777",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-iqxwbwkp",
                "SecurityGroupName": "安全组4",
                "SecurityGroupRemark": "自定义"
            },
            {
                "CreateTime": "2021-10-30 16:10:23",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "10.0.0.0/8",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "2456",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-dutt0kpv",
                "SecurityGroupName": "安全组3",
                "SecurityGroupRemark": "自定义"
            },
            {
                "CreateTime": "2021-10-30 16:09:33",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "10.0.0.0/8",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "9091",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-eudoq1bd",
                "SecurityGroupName": "安全组2",
                "SecurityGroupRemark": "自定义"
            },
            {
                "CreateTime": "2021-10-30 16:08:29",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "放通Web服务HTTP（80），如 Apache、Nginx",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "80",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "支持Ping服务",
                        "Id": "",
                        "IpProtocol": "icmp",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-fsot7c33",
                "SecurityGroupName": "安全组1",
                "SecurityGroupRemark": "自定义"
            },
            {
                "CreateTime": "2021-07-15 11:51:07",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "放通Windows远程登录",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "3389",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "::/0",
                        "Desc": "放通Windows远程登录",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "3389",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "放通Linux SSH登录",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "22",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "::/0",
                        "Desc": "放通Linux SSH登录",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "22",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "放通Web服务端口",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "80,443",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "::/0",
                        "Desc": "放通Web服务端口",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "80,443",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "放通Ping服务",
                        "Id": "",
                        "IpProtocol": "icmp",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "::/0",
                        "Desc": "放通Ping服务",
                        "Id": "",
                        "IpProtocol": "icmpv6",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "10.0.0.0/8",
                        "Desc": "放通内网",
                        "Id": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "172.16.0.0/12",
                        "Desc": "放通内网",
                        "Id": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "192.168.0.0/16",
                        "Desc": "放通内网",
                        "Id": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "0.0.0.0/0",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL",
                        "ServiceModule": ""
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "sg-fkkzqw25",
                "SecurityGroupName": "放通22，80，443，3389端口和ICMP协议-2021071511491886714",
                "SecurityGroupRemark": "公网放通云主机常用登录及web服务端口，内网全放通。"
            }
        ],
        "RequestId": "f82bd0dc-48c2-4986-8b64-d330688bed80",
        "Total": 5
    }
}
```

