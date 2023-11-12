**Example 1: 渠道商生成修改子客企业二维码链接**

渠道商生成修改子客企业二维码链接

Input: 

```
tccli essbasic ChannelCreateOrganizationModifyQrCode --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1684401637,
        "QrCodeUrl": "https://dyn.ess.tencent.cn/imgs/channelQrCodes/QrCode/yDw7aUUggsxcdcdnkncdkFtHhG1fJeu.png",
        "RequestId": "s1696921563375938822"
    }
}
```

