**Example 1: 删除admin权限**



Input: 

```
tccli tke DeleteUserPermissions --cli-unfold-argument  \
    --TargetUin 700002308532 \
    --Permissions.0.ClusterId cls-n17663rk \
    --Permissions.0.RoleName tke:admin \
    --Permissions.0.RoleType cluster \
    --Permissions.0.IsCustom False \
    --Permissions.0.Namespace 
```

Output: 
```
{
    "Response": {
        "RequestId": "eadd88e9-6a5a-48e9-828c-4cfc4bae8910"
    }
}
```

