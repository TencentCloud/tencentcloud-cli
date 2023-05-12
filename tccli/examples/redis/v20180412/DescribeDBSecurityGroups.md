**Example 1: 请求示例**

查询指定实例的安全组信息

Input: 

```
tccli redis DescribeDBSecurityGroups --cli-unfold-argument  \
    --Product redis \
    --InstanceId crs-m1kxvlkf
```

Output: 
```
{
    "Response": {
        "Groups": [
            {
                "CreateTime": "2023-04-26 17:40:29",
                "Inbound": [
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "106.55.103.75",
                        "Desc": "",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "8000",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "119.147.10.191",
                        "Desc": "bro-本地公网ip",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "8000",
                        "ServiceModule": ""
                    },
                    {
                        "Action": "ACCEPT",
                        "AddressModule": "",
                        "CidrIp": "43.136.90.27",
                        "Desc": "CVM-公网",
                        "Id": "",
                        "IpProtocol": "tcp",
                        "PortRange": "8000",
                        "ServiceModule": ""
                    }
                ],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-7y0pa6nf",
                "SecurityGroupName": "test_lb",
                "SecurityGroupRemark": "自定义"
            }
        ],
        "RequestId": "d6b8d050-f113-4db3-a85e-ca8122deddce",
        "VIP": "10.0.4.13",
        "VPort": "6379"
    }
}
```

