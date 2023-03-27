**Example 1: 示例**

示例

Input: 

```
tccli essbasic ChannelCreateUserRoles --cli-unfold-argument  \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --UserIds abc \
    --RoleIds abc
```

Output: 
```
{
    "Response": {
        "FailedCreateRoleData": [],
        "RequestId": "abc"
    }
}
```

