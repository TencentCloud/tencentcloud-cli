**Example 1: 获取成员列表**

获取成员列表

Input: 

```
tccli organization DescribeOrganizationMembers --cli-unfold-argument  \
    --Lang zh \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-04-17 12:19:07",
                "MemberType": "Invite",
                "MemberUin": 111111111111,
                "Name": "member_name",
                "NodeId": 101,
                "NodeName": "node_name",
                "IsAllowQuit": "Denied",
                "OrgPermission": [
                    {
                        "Id": 1,
                        "Name": "允许主账号查看子账号的消费信息"
                    },
                    {
                        "Id": 2,
                        "Name": "允许主账号查看子账号的财务信息"
                    }
                ],
                "OrgPolicyName": "财务管理",
                "OrgPolicyType": "Financial",
                "Remark": "member1",
                "PayUin": "",
                "PayName": "",
                "OrgIdentity": [],
                "BindStatus": "Unbound",
                "PermissionStatus": "Confirmed",
                "UpdateTime": "2021-04-17 12:19:07"
            }
        ],
        "RequestId": "a0fe0702-5757-4aa4-8872-74b70a4c1b7a",
        "Total": 1
    }
}
```

