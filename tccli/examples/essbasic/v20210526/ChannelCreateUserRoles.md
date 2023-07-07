**Example 1: 示例**

示例

Input: 

```
tccli essbasic ChannelCreateUserRoles --cli-unfold-argument  \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
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

