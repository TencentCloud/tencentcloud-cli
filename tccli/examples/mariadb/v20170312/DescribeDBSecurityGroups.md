**Example 1: 示例1 查询实例安全组信息**



Input: 

```
tccli mariadb DescribeDBSecurityGroups --cli-unfold-argument  \
    --Product mariadb \
    --InstanceId tdsql-eb2w7dto
```

Output: 
```
{
    "Response": {
        "VIP": "10.0.0.7",
        "VPort": "3306",
        "RequestId": "31a60135-7057-47ae-8fd3-7a0617deca38",
        "Groups": [
            {
                "ProjectId": 0,
                "CreateTime": "",
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
                "SecurityGroupId": "",
                "SecurityGroupName": "",
                "SecurityGroupRemark": "mariadb"
            }
        ]
    }
}
```

**Example 2: 获取实例安全组**

获取实例的详细安全组信息

Input: 

```
tccli mariadb DescribeDBSecurityGroups --cli-unfold-argument  \
    --Product mariadb \
    --InstanceId tdsql-gsv37hvp
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2024-10-23 15:57:12",
                "Inbound": [],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-52n3w8dn",
                "SecurityGroupName": "test_policy",
                "SecurityGroupRemark": ""
            },
            {
                "CreateTime": "2024-10-23 15:57:06",
                "Inbound": [],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-ljb7rq17",
                "SecurityGroupName": "test_policy",
                "SecurityGroupRemark": ""
            }
        ],
        "RequestId": "579a626b-fc7e-4726-953d-bbd1814da8b1",
        "VIP": "10.0.0.33",
        "VPort": "3306"
    }
}
```

