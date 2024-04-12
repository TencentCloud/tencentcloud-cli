**Example 1: 绑定组织成员和组织管理员子账号的授权关系**



Input: 

```
tccli organization BindOrganizationMemberAuthAccount --cli-unfold-argument  \
    --MemberUin 111111111111 \
    --PolicyId 123 \
    --OrgSubAccountUins 222222222222
```

Output: 
```
{
    "Response": {
        "RequestId": "4c2f4b68-01b2-4841-a927-6ca8fe40649b"
    }
}
```

