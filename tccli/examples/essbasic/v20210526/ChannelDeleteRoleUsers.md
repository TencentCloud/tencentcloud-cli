**Example 1: 解绑用户与角色关系**

解绑用户与角色绑定关系

Input: 

```
tccli essbasic ChannelDeleteRoleUsers --cli-unfold-argument  \
    --RoleId abc \
    --UserIds abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyAppId abc
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

