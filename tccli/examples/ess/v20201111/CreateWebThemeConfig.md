**Example 1: 增加主题配置**

增加主题配置

Input: 

```
tccli ess CreateWebThemeConfig --cli-unfold-argument  \
    --Operator.UserId userId \
    --ThemeType EMBED_WEB_THEME \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #ad352f
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

