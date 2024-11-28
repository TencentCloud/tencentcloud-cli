**Example 1: 获取组织成员的授权策略列表**



Input: 

```
tccli organization DescribeOrganizationMemberPolicies --cli-unfold-argument  \
    --MemberUin 111111111111 \
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
                "Description": "admin policy",
                "IdentityId": 1,
                "IdentityRoleAliasName": "admin",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "PolicyId": 1001,
                "PolicyName": "policy_name",
                "UpdateTime": "2021-07-14 20:22:30"
            }
        ],
        "RequestId": "a1525f09-8a00-4b76-9db5-d47aea591dff",
        "Total": 1
    }
}
```

