**Example 1: 为权限配置添加策略**

为权限配置添加策略

Input: 

```
tccli organization AddPermissionPolicyToRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-29wm2iwn \
    --RoleConfigurationId rc-aiwmsiw \
    --RolePolicyType System \
    --RolePolicyNames TestPolicy \
    --CustomPolicyDocument 
```

Output: 
```
{
    "Response": {
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

