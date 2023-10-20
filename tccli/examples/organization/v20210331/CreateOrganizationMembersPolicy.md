**Example 1: 创建组织成员访问策略**

创建组织成员访问策略

Input: 

```
tccli organization CreateOrganizationMembersPolicy --cli-unfold-argument  \
    --MemberUins 111111111111 \
    --PolicyName test \
    --IdentityId 11 \
    --Description 
```

Output: 
```
{
    "Response": {
        "PolicyId": 123,
        "RequestId": "3840f6f4-3976-4b44-9ecc-cb0578129059"
    }
}
```

