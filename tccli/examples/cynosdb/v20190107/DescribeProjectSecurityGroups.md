**Example 1: 查询项目安全组信息**



Input: 

```
tccli cynosdb DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 11954
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Groups": [
            {
                "CreateTime": "2017-04-13 15:00:06",
                "Inbound": [],
                "Outbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-ajr1jzgj",
                "SecurityGroupName": "CynosDB",
                "SecurityGroupRemark": ""
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

