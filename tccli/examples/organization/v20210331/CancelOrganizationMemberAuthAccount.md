**Example 1: 取消组织成员和组织管理员子账号的授权关系**



Input: 

```
tccli organization CancelOrganizationMemberAuthAccount --cli-unfold-argument  \
    --MemberUin 111111111111 \
    --PolicyId 123 \
    --OrgSubAccountUin 222222222222
```

Output: 
```
{
    "Response": {
        "RequestId": "caecf1a4-72b7-48d6-8f5f-90d1c428d3f3"
    }
}
```

