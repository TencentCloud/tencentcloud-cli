**Example 1: 请求示例**

查询安全组

Input: 

```
tccli redis DescribeInstanceSecurityGroup --cli-unfold-argument  \
    --InstanceIds crs-f2ho****
```

Output: 
```
{
    "Response": {
        "InstanceSecurityGroupsDetail": [
            {
                "InstanceId": "crs-f2ho****",
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
        ],
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

