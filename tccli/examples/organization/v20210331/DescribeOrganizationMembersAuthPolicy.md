**Example 1: 查询组织成员访问授权策略列表**

查询组织成员访问授权策略列表

Input: 

```
tccli organization DescribeOrganizationMembersAuthPolicy --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2022-01-13 10:27:11",
                "IdentityId": 1,
                "IdentityRoleAliasName": "Admin",
                "IdentityRoleName": "TestRole",
                "MemberName": "",
                "MemberUin": 111111111111,
                "OrgSubAccountName": "test001",
                "OrgSubAccountUin": 222222222222,
                "PolicyId": 111,
                "PolicyName": "pocy01131027"
            }
        ],
        "Total": 1,
        "RequestId": "ab3628b0-cce5-4337-9a01-e68f5242931e"
    }
}
```

