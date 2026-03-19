**Example 1: 查询实例安全组**

查询实例安全组

Input: 

```
tccli tdmysql DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId tdsql3-be88fd7f
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2024-06-14 17:54:00",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
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
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "sg-bbu5xxm3",
                "SecurityGroupName": "default",
                "SecurityGroupRemark": "System created security group"
            }
        ],
        "RequestId": "9690ec5d-4969-4bd9-ab0a-221437f617f5",
        "VIP": "10.0.0.25",
        "VPort": "3306"
    }
}
```

