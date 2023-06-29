**Example 1: 解绑用户角色**

解绑用户角色

Input: 

```
tccli ess DeleteIntegrationRoleUsers --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --RoleId yDwgKUUcXXXXXXXXXXXXXXXXXXQZxjcvkf \
    --Users.0.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZD2cds
```

Output: 
```
{
    "Response": {
        "RoleId": "yDwgKUUcXXXXXXXXXXXXXXXXXXQZxjcvkf",
        "RequestId": "abc"
    }
}
```

