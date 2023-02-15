**Example 1: 渠道版-停用印章**



Input: 

```
tccli essbasic ChannelUpdateSealStatus --cli-unfold-argument  \
    --Agent.ProxyAppId d2b****b66f954d7cc \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --SealId yDRTZxxxxxJNR \
    --Status DISABLE \
    --Reason 变更原因-停用
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

