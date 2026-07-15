**Example 1: 同步企业姓名**



Input: 

```
tccli essbasic SyncProxyOrganization --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId ke*******ng \
    --ProxyOrganizationName 典子谦示例企业
```

Output: 
```
{
    "Response": {
        "RequestId": "a4242135-81a4-46dd-b62d-9881e9d5d516"
    }
}
```

