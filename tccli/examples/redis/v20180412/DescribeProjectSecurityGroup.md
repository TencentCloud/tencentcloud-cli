**Example 1: 查询项目安全组信息**



Input: 

```
tccli redis DescribeProjectSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-gl1egaj1
```

Output: 
```
{
    "Response": {
        "RequestId": "4cc888c8-cc1c-4a77-9259-dd0f6907b559",
        "SecurityGroupDetails": [
            {
                "CreateTime": "2018-01-30 15:58:00",
                "InboundRule": [
                    {
                        "Action": "ACCEPT",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL"
                    },
                    {
                        "Action": "ACCEPT",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL"
                    }
                ],
                "OutboundRule": [
                    {
                        "Action": "ACCEPT",
                        "Ip": "0.0.0.0/0",
                        "Port": "ALL",
                        "Proto": "ALL"
                    }
                ],
                "ProjectId": 0,
                "SecurityGroupId": "sg-gl1egaj1",
                "SecurityGroupName": "all",
                "SecurityGroupRemark": ""
            }
        ]
    }
}
```

