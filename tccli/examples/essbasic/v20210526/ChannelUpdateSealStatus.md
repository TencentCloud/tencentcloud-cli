**Example 1: 停用印章**

1.指定AppId为yDwfwUUgygormhg1UuS2eARxjMT0mxAw
2.指定子客企业的OpenId为org_dianziqian
3.指定要操作的印章Id为yDRTZxxxxxJNR
4.指定设置印章状态为DISABLE

Input: 

```
tccli essbasic ChannelUpdateSealStatus --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
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

