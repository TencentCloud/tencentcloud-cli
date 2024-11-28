**Example 1: 获取组织成员被绑定授权关系的子账号列表**



Input: 

```
tccli organization DescribeOrganizationMemberAuthAccounts --cli-unfold-argument  \
    --MemberUin 111111111111 \
    --Limit 10 \
    --PolicyId 1001 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-07-14 21:00:59",
                "IdentityId": 1,
                "IdentityRoleAliasName": "admin",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "OrgSubAccountUin": 222222222222,
                "PolicyId": 1001,
                "PolicyName": "policy_name",
                "UpdateTime": "2021-07-14 21:00:59",
                "OrgSubAccountName": "sub_name"
            }
        ],
        "RequestId": "cf182a6b-8caa-4df9-b1d0-09ad41e8c434",
        "Total": 1
    }
}
```

