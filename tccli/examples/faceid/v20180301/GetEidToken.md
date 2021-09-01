**Example 1: 鉴权操作**



Input: 

```
tccli faceid GetEidToken --cli-unfold-argument  \
    --MerchantId 3232
```

Output: 
```
{
    "Response": {
        "EidToken": "CE661F1A-0F1E-45BD-BE13-34C05CEA7681",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a",
        "Url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa50a8ac379585f53&redirect_uri=https%3A%2F%2Feid.faceid.qq.com%2Fapi%2Fv1%2FGetOpenId%3Ftoken%3DCE661F1A-0F1E-45BD-BE13-34C05CEA7681&response_type=code&scope=snsapi_base&state=&component_appid=wx9802ee81e68d6dee#wechat_redirect"
    }
}
```

