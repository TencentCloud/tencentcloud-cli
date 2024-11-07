**Example 1: 删除角色**

根据角色id删除角色

Input: 

```
tccli essbasic ChannelDeleteRole --cli-unfold-argument  \
    --Agent.AppId  yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --RoleIds yDxZ1UyKQDSIMfUuO4zjEw2TyqzKEs16
```

Output: 
```
{
    "Response": {
        "RequestId": " 49500cb4-ca5e-4da0-93fb-e15f3a710ed7"
    }
}
```

