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
                "Name": "test2",
                "NodeId": 27,
                "NodeName": "node1",
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
                "Remark": "123",
                "PayUin": "",
                "PayName": "",
                "OrgIdentity": [],
                "BindStatus": "Unbound",
                "PermissionStatus": "Confirmed",
                "UpdateTime": "2021-04-17 12:19:07"
            },
            {
                "CreateTime": "2021-04-16 11:49:39",
                "MemberType": "Create",
                "MemberUin": 222222222222,
                "Name": "name2",
                "NodeId": 26,
                "NodeName": "node2",
                "IsAllowQuit": "Denied",
                "OrgPermission": [
                    {
                        "Id": 1,
                        "Name": "允许主账号查看子账号的消费信息"
                    },
                    {
                        "Id": 2,
                        "Name": "允许主账号查看子账号的财务信息"
                    },
                    {
                        "Id": 3,
                        "Name": "允许主账号划拨资金给子账号"
                    },
                    {
                        "Id": 4,
                        "Name": "允许主账号对子账号的账单合并出账"
                    },
                    {
                        "Id": 5,
                        "Name": "允许主账号代子账号开票"
                    }
                ],
                "OrgPolicyName": "财务管理",
                "OrgPolicyType": "Financial",
                "Remark": "",
                "PayUin": "",
                "PayName": "",
                "OrgIdentity": [],
                "BindStatus": "Unbound",
                "PermissionStatus": "Confirmed",
                "UpdateTime": "2021-04-16 11:49:39"
            }
        ],
        "RequestId": "a0fe0702-5757-4aa4-8872-74b70a4c1b7a",
        "Total": 2
    }
}
```

