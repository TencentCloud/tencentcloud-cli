**Example 1: 获取组织成员被绑定授权关系的子账号列表**



Input: 

```
tccli organization DescribeOrganizationMemberAuthAccounts --cli-unfold-argument  \
    --MemberUin 111111111111 \
    --Limit 10 \
    --PolicyId 11 \
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
                "IdentityRoleAliasName": "登录访问",
                "IdentityRoleName": "OrganizationAccessControlRole",
                "OrgSubAccountUin": 100000546921,
                "PolicyId": 98081,
                "PolicyName": "test",
                "UpdateTime": "2021-07-14 21:00:59",
                "OrgSubAccountName": "test"
            }
        ],
        "RequestId": "cf182a6b-8caa-4df9-b1d0-09ad41e8c434",
        "Total": 1
    }
}
```

