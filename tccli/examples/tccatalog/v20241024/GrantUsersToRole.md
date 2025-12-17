**Example 1: 批量绑定用户到某个角色**



Input: 

```
tccli tccatalog GrantUsersToRole --cli-unfold-argument  \
    --RoleId 100008882713 \
    --PlatformIds 100008882712 100008882714
```

Output: 
```
{
    "Response": {
        "RequestId": "a89b45d2-6e3f-4a7c-b8d2-5f1e6d9c8a7b"
    }
}
```

