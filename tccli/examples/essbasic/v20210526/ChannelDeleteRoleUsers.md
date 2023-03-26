**Example 1: 解绑用户与角色关系**

解绑用户与角色绑定关系

Input: 

```
tccli essbasic ChannelDeleteRoleUsers --cli-unfold-argument  \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --RoleId abc \
    --UserIds abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc
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

