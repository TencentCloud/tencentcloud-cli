**Example 1: 创建用户**



Input: 

```
tccli evt CreateRoleUser --cli-unfold-argument  \
    --RoleSystemId 81764213873244 \
    --UserId user \
    --Username name \
    --Enabled 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e56eec58-c446-44d0-917b-a0df066a4f50",
        "UserId": "user"
    }
}
```

