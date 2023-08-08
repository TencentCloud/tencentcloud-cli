**Example 1: 绑定用户角色**

绑定用户角色

Input: 

```
tccli essbasic ChannelCreateUserRoles --cli-unfold-argument  \
    --Agent.AppId sdkdk78193cksc9s***k9dfk \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --UserIds ywksdkj1001***103kd \
    --RoleIds ywk9kdki323****k239239
```

Output: 
```
{
    "Response": {
        "FailedCreateRoleData": [],
        "RequestId": " s129023***12003023"
    }
}
```

