**Example 1: 获取跳转链接**

获取开通个人自动签跳转链接

Input: 

```
tccli essbasic ChannelCreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.ClientIp  \
    --Operator.CustomUserId  \
    --Operator.ProxyIp  \
    --Operator.Channel  \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --AutoSignConfig.UserInfo.Name 小明 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 1xxxxxxxxxxxxxx0 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal False \
    --AutoSignConfig.SealImgCallback False \
    --AutoSignConfig.CallbackUrl 
```

Output: 
```
{
    "Response": {
        "AppId": "wxa02378y4jruwye1d",
        "AppOriginalId": "gh_da87293fsd87987",
        "Path": "page?abc=123&def=456",
        "QrCode": "EBAQAAAAAAAAAAAQIDBAUGBwgJCgsQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCN",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://xxx.xxx/abc123",
        "UrlType": ""
    }
}
```

