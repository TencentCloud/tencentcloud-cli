**Example 1: 获取组织成员的授权策略列表**



Input: 

```
tccli organization DescribeOrganizationMemberPolicies --cli-unfold-argument  \
    --MemberUin 100000546922 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-07-14 20:22:30",
                "Description": "test",
                "IdentityId": 1,
                "IdentityRoleAliasName": "登录访问",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "PolicyId": 27887,
                "PolicyName": "test3",
                "UpdateTime": "2021-07-14 20:22:30"
            },
            {
                "CreateTime": "2021-07-14 20:21:21",
                "Description": "test",
                "IdentityId": 1,
                "IdentityRoleAliasName": "登录访问",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "PolicyId": 98081,
                "PolicyName": "test",
                "UpdateTime": "2021-07-14 20:21:21"
            }
        ],
        "RequestId": "a1525f09-8a00-4b76-9db5-d47aea591dff",
        "Total": 2
    }
}
```

