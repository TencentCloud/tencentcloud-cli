**Example 1: 检查用户是否被授予某个角色**



Input: 

```
tccli tccatalog CheckUserRoleGranted --cli-unfold-argument  \
    --RoleName admin
```

Output: 
```
{
    "Response": {
        "Granted": true,
        "RequestId": "d6e4a9b1-7f2c-4a8d-b5e3-1c9f8a6b2d0e"
    }
}
```

