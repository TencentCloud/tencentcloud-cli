**Example 1: 获取组织成员可被管理的身份列表**

获取组织成员可被管理的身份列表

Input: 

```
tccli organization DescribeOrganizationMemberAuthIdentities --cli-unfold-argument  \
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
                "CreateTime": "2021-07-14 20:17:34",
                "Description": "AdministratorAccess",
                "IdentityId": 1,
                "IdentityRoleAliasName": "登录访问",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "IdentityType": 1,
                "UpdateTime": "2021-07-14 20:17:34"
            }
        ],
        "RequestId": "55fa3e27-1166-45e1-bdac-6198c3c38534",
        "Total": 1
    }
}
```

