**Example 1: 创建主题配置**

创建主题配置： 展示腾讯电子签的logo，红色主题

Input: 

```
tccli ess CreateWebThemeConfig --cli-unfold-argument  \
    --Operator.UserId 195xxxxxxxxxxxxxxxde6a \
    --ThemeType EMBED_WEB_THEME \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #ad352f
```

Output: 
```
{
    "Response": {
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
    }
}
```

**Example 2: 创建主题配置：不支持的主题类型**

不支持的主题类型

Input: 

```
tccli ess CreateWebThemeConfig --cli-unfold-argument  \
    --Operator.UserId 195xxxxxxxxxxxxxxxde6a \
    --ThemeType EMBED \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #ad352f
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied",
            "Message": "不支持的主题类型"
        },
        "RequestId": "43b9474a-c909-4d89-aa7b-3632f02fa8a4"
    }
}
```

