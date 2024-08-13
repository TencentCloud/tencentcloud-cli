**Example 1: 获取权限配置中的策略列表**

获取权限配置中的策略列表

Input: 

```
tccli organization ListPermissionPoliciesInRoleConfiguration --cli-unfold-argument  \
    --ZoneId z-d83js823n \
    --RoleConfigurationId rc-s93jw3ns \
    --RolePolicyType System
```

Output: 
```
{
    "Response": {
        "TotalCounts": 20,
        "RolePolicies": [
            {
                "RolePolicyName": "adminPolciy",
                "RolePolicyType": "System",
                "RolePolicyDocument": "",
                "AddTime": "2020-01-01 12:12:12"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

