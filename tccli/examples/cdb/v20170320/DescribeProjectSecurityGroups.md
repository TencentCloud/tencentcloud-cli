**Example 1: 查询项目安全组信息**



Input: 

```
tccli cdb DescribeProjectSecurityGroups --cli-unfold-argument  \
    --ProjectId 11954
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Groups": [
            {
                "Outbound": [],
                "SecurityGroupName": "CDB",
                "Inbound": [],
                "ProjectId": 0,
                "SecurityGroupId": "sg-xx",
                "SecurityGroupRemark": "",
                "CreateTime": "2017-04-13 15:00:06"
            }
        ]
    }
}
```

