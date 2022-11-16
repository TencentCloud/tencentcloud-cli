**Example 1: 创建组织成员访问授权策略**



Input: 

```
tccli organization CreateOrganizationMemberPolicy --cli-unfold-argument  \
    --PolicyName test \
    --MemberUin 100000546922 \
    --Description test \
    --IdentityId 1
```

Output: 
```
{
    "Response": {
        "PolicyId": 98081,
        "RequestId": "a1a10c6e-6723-408a-858b-2cb84e92776c"
    }
}
```

