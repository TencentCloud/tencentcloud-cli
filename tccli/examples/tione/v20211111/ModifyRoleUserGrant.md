**Example 1: 更新用户角色绑定**



Input: 

```
tccli tione ModifyRoleUserGrant --cli-unfold-argument  \
    --TiProjectId 1889353273052233728 \
    --RoleIds developer \
    --SubUins 100032950128 \
    --Grant BIND
```

Output: 
```
{
    "Response": {
        "RequestId": "558ac640-ea9f-4080-9fa8-6fd120c30cdd"
    }
}
```

