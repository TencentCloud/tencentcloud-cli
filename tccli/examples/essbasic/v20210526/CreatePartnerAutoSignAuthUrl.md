**Example 1: 授权给渠道平台应用**



Input: 

```
tccli essbasic CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDSxxxxxxxxxOnHtH51 \
    --Agent.ProxyOrganizationOpenId org_open_id \
    --Agent.ProxyOperator.OpenId user_open_id \
    --AuthorizedOrganizationId org_open_id_another \
    --AuthorizedOrganizationName 典子谦子客企业 \
    --PlatformAppAuthorization True
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1702982931,
        "MiniAppPath": "/pages/guide/index?shortKey=yDSxxxxxxxxxOnHtH51",
        "RequestId": "s1702378131281988373",
        "Url": "https://test.essurl.cn/WxxxxxwH"
    }
}
```

**Example 2: 创建他方自动签授权链接**



Input: 

```
tccli essbasic CreatePartnerAutoSignAuthUrl --cli-unfold-argument  \
    --Agent.AppId yDSxxxxxxxxxOnHtH51 \
    --Agent.ProxyOrganizationOpenId org_open_id \
    --Agent.ProxyOperator.OpenId user_open_id \
    --AuthorizedOrganizationId org_open_id_another \
    --AuthorizedOrganizationName 典子谦子客企业
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1702982931,
        "MiniAppPath": "/pages/guide/index?shortKey=yDSxxxxxxxxxOnHtH51",
        "RequestId": "s1702378131281988373",
        "Url": "https://test.essurl.cn/WxxxxxwH"
    }
}
```

