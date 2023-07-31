**Example 1: 生成嵌入式主题**

生成嵌入式主题

Input: 

```
tccli essbasic ChannelCreateWebThemeConfig --cli-unfold-argument  \
    --Agent.AppId yDRsbUUgy***y8lsS7ZfBvipOMJ \
    --Agent.ProxyAppId yDRTvUUgyg***7yEkoMkHXm \
    --Agent.ProxyOperator.OpenId 5d18c1c4****--3a0c8926cd11 \
    --Agent.ProxyOrganizationOpenId 572c69b2-****-14e06d1245e4 \
    --ThemeType EMBED_WEB_THEME \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #4de813
```

Output: 
```
{
    "Response": {
        "RequestId": "s169*****642528438"
    }
}
```

