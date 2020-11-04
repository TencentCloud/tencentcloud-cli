**Example 1: 查询实例安全组信息**



Input: 

```
tccli cynosdb DescribeDBSecurityGroups --cli-unfold-argument  \
    --InstanceId cynosdbpg-ins-jhi2gdi0
```

Output: 
```
{
    "Response": {
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

