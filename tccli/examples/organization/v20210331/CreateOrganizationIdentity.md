**Example 1: 添加组织身份**



Input: 

```
tccli organization CreateOrganizationIdentity --cli-unfold-argument  \
    --Description  \
    --IdentityAliasName test \
    --IdentityPolicy.0.PolicyId 1 \
    --IdentityPolicy.0.PolicyName AdministratorAccess
```

Output: 
```
{
    "Response": {
        "IdentityId": 123,
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

