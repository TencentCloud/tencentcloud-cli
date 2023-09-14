**Example 1: 生成嵌入式主题**

生成嵌入式主题

Input: 

```
tccli essbasic ChannelCreateWebThemeConfig --cli-unfold-argument  \
    --Agent.AppId yDRsbUUgy***y8lsS7ZfBvipOMJ \
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

**Example 2: 生成嵌入式主题：不支持的主题类型**

不支持的主题类型

Input: 

```
tccli essbasic ChannelCreateWebThemeConfig --cli-unfold-argument  \
    --Agent.AppId yDRsbUUgy***y8lsS7ZfBvipOMJ \
    --Agent.ProxyOperator.OpenId 5d18c1c4****--3a0c8926cd11 \
    --Agent.ProxyOrganizationOpenId 572c69b2-****-14e06d1245e4 \
    --ThemeType EMBED \
    --WebThemeConfig.DisplaySignBrandLogo True \
    --WebThemeConfig.WebEmbedThemeColor #4de813
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

