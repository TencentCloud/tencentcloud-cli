**Example 1: 停用印章**

停用子客企业的印章

Input: 

```
tccli essbasic ChannelUpdateSealStatus --cli-unfold-argument  \
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
        "RequestId": "s187098654322345"
    }
}
```

