**Example 1: 获取跳转链接**

获取跳转链接

Input: 

```
tccli ess CreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.UserId 123 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --AutoSignConfig.UserInfo.Name 小明 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 1xxxxxxxxxxxxxx0 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal False \
    --AutoSignConfig.SealImgCallback False \
    --AutoSignConfig.CallbackUrl  \
    --AutoSignConfig.VerifyChannels  \
    --UrlType 
```

Output: 
```
{
    "Response": {
        "AppId": "wxa02378y4jruwye1d",
        "AppOriginalId": "gh_da87293fsd87987",
        "Path": "page?abc=123&def=456",
        "QrCode": "EBAQAAAAAAAAAAAQIDBAUGBwgxxxxxwAEEQUSITFBBhNRYQcicRQygZGhCCN",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://xxx.xxx/abc123",
        "UrlType": ""
    }
}
```

