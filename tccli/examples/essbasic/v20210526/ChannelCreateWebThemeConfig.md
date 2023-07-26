**Example 1: 生成嵌入式主题**

生成嵌入式主题

Input: 

```
tccli essbasic ChannelCreateWebThemeConfig --cli-unfold-argument  \
    --ThemeType ThemeType_EMBED_WEB_THEME \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #ad352f \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

