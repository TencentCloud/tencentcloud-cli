**Example 1: 删除指定印章下多个授权信息**

删除指定印章下多个授权信息

Input: 

```
tccli essbasic ChannelDeleteSealPolicies --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --SealId yDRTZxxxxxJNR \
    --UserIds yDxxxTZxxxxxJNR
```

Output: 
```
{
    "Response": {
        "RequestId": "yDasdfasdfxxxxxJNR"
    }
}
```

