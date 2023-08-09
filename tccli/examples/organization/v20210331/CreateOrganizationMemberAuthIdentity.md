**Example 1: 添加组织成员访问授权**

添加组织成员访问授权

Input: 

```
tccli organization CreateOrganizationMemberAuthIdentity --cli-unfold-argument  \
    --MemberUins 111111111111 \
    --IdentityIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3840f6f4-3976-4b44-9ecc-cb0578129059"
    }
}
```

