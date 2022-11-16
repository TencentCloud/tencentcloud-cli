**Example 1: 取消成员和子账号的授权关系**



Input: 

```
tccli organization CancelOrganizationMemberAuthAccount --cli-unfold-argument  \
    --MemberUin 100000546922 \
    --PolicyId 98081 \
    --OrgSubAccountUin 100000546921
```

Output: 
```
{
    "Response": {
        "RequestId": "caecf1a4-72b7-48d6-8f5f-90d1c428d3f3"
    }
}
```

