**Example 1: 解绑用户角色**

解绑用户角色

Input: 

```
tccli ess DeleteIntegrationRoleUsers --cli-unfold-argument  \
    --Operator.UserId abc \
    --Operator.Channel abc \
    --Operator.OpenId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --RoleId abc \
    --Users.0.UserId abc \
    --Agent.AppId abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --Agent.ProxyOperator abc
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

