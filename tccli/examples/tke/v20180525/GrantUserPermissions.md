**Example 1: 授予admin权限**



Input: 

```
tccli tke GrantUserPermissions --cli-unfold-argument  \
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
        "RequestId": "d2be08f4-dbf9-420b-aeaa-108ce91ce0f0"
    }
}
```

