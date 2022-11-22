**Example 1: 示例1 查询项目安全组信息**



Input: 

```
tccli dcdb DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 11954 \
    --Product dcdb
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "31a60135-7057-47ae-8fd3-7a0617deca38",
        "Groups": [
            {
                "ProjectId": 11988,
                "CreateTime": "2017-04-13 15:00:06",
                "Inbound": [
                    {
                        "Action": "",
                        "CidrIp": "",
                        "PortRange": "",
                        "IpProtocol": ""
                    }
                ],
                "Outbound": [
                    {
                        "Action": "",
                        "CidrIp": "",
                        "PortRange": "",
                        "IpProtocol": ""
                    }
                ],
                "SecurityGroupId": "sg-ajr1jzgj",
                "SecurityGroupName": "dcdb",
                "SecurityGroupRemark": ""
            }
        ]
    }
}
```

