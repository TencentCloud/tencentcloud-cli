**Example 1: 获取设置自动签印章的小程序链接。**

1. 用户已经开通自动签。
2. 获取设置自动签印章的小程序链接。

Input: 

```
tccli ess CreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.IdCardNumber 620000198802020000 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 典子谦
```

Output: 
```
{
    "Response": {
        "AppId": "wxa023******e1d",
        "AppOriginalId": "gh_da87*******987",
        "Path": "page?abc=123&def=456",
        "QrCode": "EBAQAAAAAAAAAAAQIDBAUGBwgxxxxxwAEEQUSITFBBhNRYQcicRQygZGhCCN",
        "RequestId": "s169563****093",
        "Url": "https://essurl.cn/dKd**6ZCh"
    }
}
```

**Example 2: 错误示例-获取设置自动签印章的小程序链接。**

1. 用户没有开通自动签。

Input: 

```
tccli ess CreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Operator.ClientIp 1.2.3.4 \
    --Operator.UserId yDRCLUUgygq2xu********Ewg0vjoimj \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.IdCardNumber 37000019890303000X \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.Name 张三
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "用户未开通自动签"
        },
        "RequestId": "s16***55712"
    }
}
```

**Example 3: 获取设置自动签印章的小程序长链接。**

1. 用户已经开通自动签。
2. 获取设置自动签印章的小程序链接。
3.设置EndPoint=HTTP

Input: 

```
tccli ess CreateUserAutoSignSealUrl --cli-unfold-argument  \
    --Operator.UserId yDwgGUUckp1pgi0zUEfxo8AB2PEWmWZL \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 刘付彩文 \
    --UserInfo.IdCardType ID_CARD \
    --UserInfo.IdCardNumber 440982199707195371 \
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
        "Url": "https://res.ess.tencent.cn/cdn/h5-activity-dev/jump-mp.html?to=KA_AUTO_ESIGN_MODIFY&channel=autoSign&identityChange=0&organizationId=yDwf3UUckpshchk9Uuan1OkFOE0qLixm&sceneKey=E_PRESCRIPTION_AUTO_SIGN&confToken=yD3JcUUckpepfv1yU0WZWMpDKfYS68Wu",
        "RequestId": "2c2a4cff-ce6f-4e77-95f8-69588569aab4"
    }
}
```

