**Example 1: 示例**

示例

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
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
    --Filters.0.Key abc \
    --Filters.0.Values abc \
    --Offset 1 \
    --Limit abc
```

Output: 
```
{
    "Response": {
        "Offset": 1,
        "Limit": 1,
        "TotalCount": 1,
        "ChannelRoles": [
            {
                "RoleId": "abc",
                "RoleName": "abc",
                "RoleStatus": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

