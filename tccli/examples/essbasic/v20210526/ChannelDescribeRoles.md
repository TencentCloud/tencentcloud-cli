**Example 1: 查询角色列表**

查询角色列表

Input: 

```
tccli essbasic ChannelDescribeRoles --cli-unfold-argument  \
    --Agent.AppId  jsdk812kxkdfjks***k88123123 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --Filters.0.Key  \
    --Filters.0.Values  \
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
                "RoleId": "abc8jkkjds***121212",
                "RoleName": "业务管理员",
                "RoleStatus": 1
            }
        ],
        "RequestId": " s19ksdjkkds****ldsjfkdfdf"
    }
}
```

