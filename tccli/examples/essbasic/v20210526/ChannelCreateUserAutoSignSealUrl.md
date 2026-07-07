**Example 1: 获取设置个人自动签印章的小程序链接。**

1. 企业已经开通自动签功能。
2. 个人已经开通自动签。

Input: 

```
tccli essbasic ChannelCreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.IdCardNumber 1xxxxxxxxxxxxxx0 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 小明
```

Output: 
```
{
    "Response": {
        "AppId": "wxa023******e1d",
        "AppOriginalId": "gh_da87*******987",
        "Path": "page?abc=123&def=456",
        "QrCode": "EBAQAAAAAAAAAAAQIDBAUGBwgxxxxxwAEEQUSITFBBhNRYQcicRQygZGhCCN",
        "RequestId": "s1695****69",
        "Url": "https://essurl.cn/vg****6YYG"
    }
}
```

**Example 2: 错误示例-获取设置个人自动签印章链接，个人没有开通自动签。**

1. 企业开通自动签。
2. 个人没有开通自动签。

Input: 

```
tccli essbasic ChannelCreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.IdCardNumber 1xxxxxxxxxxxxxx0 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 小明
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "用户未开通自动签"
        },
        "RequestId": "s169***148251031"
    }
}
```

**Example 3: 获取设置个人自动签印章的小程序长链接。**

1. 企业已经开通自动签功能。
2. 个人已经开通自动签。
3.将参数EndPoint设置为HTTP

Input: 

```
tccli essbasic ChannelCreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Agent.AppId yDwFoUUckpsomwx1UyhWGhIR2RkhOjw2 \
    --Agent.ProxyOrganizationOpenId ess_open_organization_1 \
    --Agent.ProxyOperator.OpenId kevinlcheng \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 刘付彩文 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.IdCardNumber 440982199707195371 \
    --Operator.OpenId  \
    --EndPoint HTTP
```

Output: 
```
{
    "Response": {
        "AppId": "",
        "AppOriginalId": "",
        "Path": "",
        "QrCode": "",
        "Url": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=KA_AUTO_ESIGN_MODIFY&channel=autoSign&identityChange=0&organizationId=yDwFmUUckpstjt1aUyN9xSlvgkLEa4NC&sceneKey=E_PRESCRIPTION_AUTO_SIGN&confToken=yD3JcUUckpepm1maUy4y9iHw6yuotr7l",
        "RequestId": "85ecfeb6-974a-45d2-ba6e-a4ed27b30116"
    }
}
```

