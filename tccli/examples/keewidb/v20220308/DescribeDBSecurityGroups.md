**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --Product keewidb
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
                "SecurityGroupId": "sg-iqxw****",
                "SecurityGroupName": "安全组4",
                "SecurityGroupRemark": "自定义"
            }
        ],
        "RequestId": "6bb17fcf-dd09-440b-806b-198261cff9a1",
        "VIP": "10.0.16.44",
        "VPort": "6379"
    }
}
```

