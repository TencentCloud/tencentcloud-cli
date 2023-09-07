**Example 1: 获取H5开通跳转链接**

将UrlType参数设置为 H5SIGN，即可获得H5页面开通链接

Input: 

```
tccli ess CreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --AutoSignConfig.UserInfo.Name 典子谦 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 620000198802020000 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal True \
    --AutoSignConfig.SealImgCallback True \
    --AutoSignConfig.CallbackUrl http://www.example.com \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UrlType H5SIGN
```

Output: 
```
{
    "Response": {
        "AppId": "",
        "AppOriginalId": "",
        "Path": "",
        "QrCode": "",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://essurl.cn/q5nQ*CSFBZ",
        "UrlType": "H5SIGN"
    }
}
```

**Example 2: 获取小程序跳转链接**

UrlType参数是用来控制生成链接类型的，如果不传，则默认生成小程序跳转链接

Input: 

```
tccli ess CreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --AutoSignConfig.UserInfo.Name 典子谦 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 620000198802020000 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal True \
    --AutoSignConfig.SealImgCallback True \
    --AutoSignConfig.CallbackUrl http://www.example.com \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UrlType 
```

Output: 
```
{
    "Response": {
        "AppId": "wxa023******e1d",
        "AppOriginalId": "gh_da87*******987",
        "Path": "page?abc=123&def=456",
        "QrCode": "EBAQAAAAAAAAAAAQIDBAUGBwgxxxxxwAEEQUSITFBBhNRYQcicRQygZGhCCN",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://essurl.cn/q5nQ*CSFBZ",
        "UrlType": ""
    }
}
```

**Example 3: 设置用户开通认证校验方式**

通过 AutoSignConfig.VerifyChannels 参数，可以控制用户在开通的时候所使用的认证方式。以下例子为生成用户短信验证开通的链接为例，链接类型为H5跳转链接。

Input: 

```
tccli ess CreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --AutoSignConfig.UserInfo.Name 典子谦 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 620000198802020000 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal True \
    --AutoSignConfig.SealImgCallback True \
    --AutoSignConfig.CallbackUrl http://www.example.com \
    --AutoSignConfig.VerifyChannels TELECOM \
    --NotifyType SMS \
    --NotifyAddress 13200000000 \
    --ExpiredTime 1693290580 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UrlType H5SIGN
```

Output: 
```
{
    "Response": {
        "AppId": "",
        "AppOriginalId": "",
        "Path": "",
        "QrCode": "",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://essurl.cn/q5nQ*CSFBZ",
        "UrlType": "H5SIGN"
    }
}
```

**Example 4: 通知对应开通用户以及设置过期时间**

可以使用短信通知用户点击链接进行开通，短信中的链接跳转到小程序或者H5取决于UrlType参数。下面的例子将使用H5跳转链接为例。
过期时间需要使用时间戳类型进行设置，要求请参考 "ExpiredTime" 参数。

Input: 

```
tccli ess CreateUserAutoSignEnableUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --AutoSignConfig.UserInfo.Name 典子谦 \
    --AutoSignConfig.UserInfo.IdCardType ID_CARD \
    --AutoSignConfig.UserInfo.IdCardNumber 620000198802020000 \
    --AutoSignConfig.CertInfoCallback True \
    --AutoSignConfig.UserDefineSeal True \
    --AutoSignConfig.SealImgCallback True \
    --AutoSignConfig.CallbackUrl http://www.example.com \
    --NotifyType SMS \
    --NotifyAddress 13200000000 \
    --ExpiredTime 1693290580 \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UrlType H5SIGN
```

Output: 
```
{
    "Response": {
        "AppId": "",
        "AppOriginalId": "",
        "Path": "",
        "QrCode": "",
        "RequestId": "5beb5f54-cf3d-4c26-a4ee-a97c85196a3e",
        "Url": "https://essurl.cn/q5nQ*CSFBZ",
        "UrlType": "H5SIGN"
    }
}
```

