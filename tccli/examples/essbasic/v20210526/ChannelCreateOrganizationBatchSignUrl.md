**Example 1: 创建签署链接**

待签署的合同

Input: 

```
tccli essbasic ChannelCreateOrganizationBatchSignUrl --cli-unfold-argument  \
    --Agent.AppId 60exxxxxxxxxxxxxxxxxxxxxc16e9 \
    --Agent.ProxyOrganizationOpenId org_open_id \
    --Name  \
    --Mobile  \
    --FlowIds yDxxxxxxxxxxxxxxxxxxxxxxxx \
    --OpenId user_open_id
```

Output: 
```
{
    "Response": {
        "SignUrl": "https://embed.test.qian.tencent.cn/console/?channel=PROXYCHANNEL&expiredTime=1695805069&code=xxxxx&menuStatus=ENABLE&token=xxxx",
        "ExpiredTime": 0,
        "RequestId": "s1695804769054178191"
    }
}
```

