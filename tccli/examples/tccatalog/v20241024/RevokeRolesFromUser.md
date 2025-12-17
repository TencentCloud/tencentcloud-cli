**Example 1: 批量解绑角色到某个用户**



Input: 

```
tccli tccatalog RevokeRolesFromUser --cli-unfold-argument  \
    --PlatformId 100008882712 \
    --RoleIds 100008882713 100008882714
```

Output: 
```
{
    "Response": {
        "RequestId": "c7f3a8d2-5e42-4f7a-b1c6-9d3e5f6a7890"
    }
}
```

