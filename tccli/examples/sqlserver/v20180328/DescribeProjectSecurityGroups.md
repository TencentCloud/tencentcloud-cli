**Example 1: 查询项目安全组信息**



Input: 

```
tccli sqlserver DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "48a7b046-479f-4f8d-8c34-e6615aec5b73",
        "SecurityGroupSet": [
            {
                "CreateTime": "2019-03-29 12:01:40",
                "InboundSet": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Dir": "INPUT",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "OutboundSet": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "Dir": "OUTPUT",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "sg-igw86yth",
                "SecurityGroupName": "default",
                "SecurityGroupRemark": "System created security group"
            }
        ]
    }
}
```

