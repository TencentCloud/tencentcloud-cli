**Example 1: 请求示例**



Input: 

```
tccli redis DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 11954 \
    --Product redis
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A1",
        "Groups": [
            {
                "Outbound": [],
                "SecurityGroupName": "CDB",
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

