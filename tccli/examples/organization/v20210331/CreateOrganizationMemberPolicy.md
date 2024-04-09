**Example 1: 创建组织成员访问授权策略**



Input: 

```
tccli organization CreateOrganizationMemberPolicy --cli-unfold-argument  \
    --PolicyName policy_name \
    --MemberUin 111111111111 \
    --Description description \
    --IdentityId 11
```

Output: 
```
{
    "Response": {
        "PolicyId": 123,
        "RequestId": "a1a10c6e-6723-408a-858b-2cb84e92776c"
    }
}
```

