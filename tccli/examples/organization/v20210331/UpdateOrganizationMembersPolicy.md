**Example 1: 修改组织成员访问策略**



Input: 

```
tccli organization UpdateOrganizationMembersPolicy --cli-unfold-argument  \
    --MemberUins 111111111111 \
    --PolicyId 101 \
    --IdentityId 11 \
    --Description admin policy
```

Output: 
```
{
    "Response": {
        "RequestId": "a4868f21-fa38-4815-8e48-596b17c1b37"
    }
}
```

