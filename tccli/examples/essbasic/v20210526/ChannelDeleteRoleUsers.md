**Example 1: 解绑用户与角色关系**

解绑用户与角色绑定关系

Input: 

```
tccli essbasic ChannelDeleteRoleUsers --cli-unfold-argument  \
    --RoleId ywkdkfd****sdkljfks \
    --UserIds ywd8k13jkds****39kdf \
    --Agent.AppId ab3kdj3kv9deal0***kdf8d89 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid
```

Output: 
```
{
    "Response": {
        "RoleId": "ywkdkfd****sdkljfks",
        "RequestId": "s1d8k2348dskfsj***kcnk"
    }
}
```

