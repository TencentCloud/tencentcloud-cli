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

