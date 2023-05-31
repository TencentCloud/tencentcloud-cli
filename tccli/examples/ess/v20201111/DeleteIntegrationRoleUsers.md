**Example 1: 解绑用户角色**

解绑用户角色

Input: 

```
tccli ess DeleteIntegrationRoleUsers --cli-unfold-argument  \
    --Operator.UserId abc \
    --RoleId abc \
    --Users.0.UserId abc
```

Output: 
```
{
    "Response": {
        "RoleId": "abc",
        "RequestId": "abc"
    }
}
```

