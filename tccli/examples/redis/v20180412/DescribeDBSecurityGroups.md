**Example 1: 示例**



Input: 

```
tccli redis DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId crs-eb2w7dto \
    --Product redis
```

Output: 
```
{
    "Response": {
        "VIP": "10.10.0.1",
        "VPort": "6379",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A1",
        "Groups": [
            {
                "Outbound": [],
                "SecurityGroupName": "Redis安全组",
                "Inbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-ajr1jzgj",
                "SecurityGroupRemark": "",
                "CreateTime": "2017-04-13 15:00:06"
            }
        ]
    }
}
```

