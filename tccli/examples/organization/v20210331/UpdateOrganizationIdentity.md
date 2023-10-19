**Example 1: 更新组织身份**



Input: 

```
tccli organization UpdateOrganizationIdentity --cli-unfold-argument  \
    --Description  \
    --IdentityId 1 \
    --IdentityPolicy.0.PolicyId 1 \
    --IdentityPolicy.0.PolicyName AdministratorAccess
```

Output: 
```
{
    "Response": {
        "RequestId": "b46d2afe-6893-4529-bc96-2c82d9214957"
    }
}
```

