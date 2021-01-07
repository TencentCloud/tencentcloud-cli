**Example 1: 示例1 查询项目安全组信息**



Input: 

```
tccli mariadb DescribeProjectSecurityGroups --cli-unfold-argument  \
    --Product mariadb \
    --ProjectId 11988
```

Output: 
```
{
    "Response": {
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
                "SecurityGroupName": "mariadb",
                "SecurityGroupRemark": ""
            }
        ]
    }
}
```

