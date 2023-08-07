**Example 1: 解绑用户角色**

解绑用户角色

Input: 

```
tccli ess DeleteIntegrationRoleUsers --cli-unfold-argument  \
    --Operator.UserId yDwgKUUc*********QZDRuD \
    --RoleId yDwgKUUc**********QZxjcvkf \
    --Users.0.UserId yDwgKUUc********QZD2cds
```

Output: 
```
{
    "Response": {
        "RoleId": "yDwgKUUc********QZxjcvkf",
        "RequestId": "s89su8dfjkdj****kdjfdfdfd"
    }
}
```

