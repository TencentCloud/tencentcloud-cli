**Example 1: 查询节点安全组信息**

本接口（DescribeDBCustomNodeSecurityGroups）用于查询DB Custom节点的安全组

Input: 

```
tccli dbdc DescribeDBCustomNodeSecurityGroups --cli-unfold-argument  \
    --NodeId dbcn-4ngxncm5
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2026-07-23 11:23:06",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "CidrIp": "0.0.0.0/0",
                        "IpProtocol": "ALL",
                        "PortRange": "ALL"
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-ibp49iqt",
                "SecurityGroupName": "wanquan_sg_2",
                "SecurityGroupRemark": "自定义"
            }
        ],
        "RequestId": "f877dee4-4060-4dba-b1f4-1fb6e7de83ef"
    }
}
```

