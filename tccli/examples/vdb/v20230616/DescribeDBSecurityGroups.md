**Example 1: 示例1**

查询实例安全组

Input: 

```
tccli vdb DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId vdb-77qt0r46
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2023-07-03 11:41:46",
                "Inbound": [
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
                        "CidrIp": "::/0",
                        "Desc": "放通Linux SSH登录",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "22",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [
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
                "ProjectId": "0",
                "SecurityGroupId": "sg-9hb3ijfx",
                "SecurityGroupName": "安全组4",
                "SecurityGroupRemark": "测试安全组",
                "UpdateTime": "2023-07-03 11:41:49"
            }
        ],
        "RequestId": "3bd8eb38-516f-44f3-b127-40e9f83f9793"
    }
}
```

