**Example 1: 查询实例安全组信息**



Input: 

```
tccli sqlserver DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId mssql-6f4ddx2f
```

Output: 
```
{
    "Response": {
        "RequestId": "1531f8ed-b13f-430b-b6a6-d85474877f3f",
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

