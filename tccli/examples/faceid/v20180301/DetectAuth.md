**Example 1: 鉴权操作 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=DetectAuth&SignVersion=)**



Input: 

```
tccli faceid DetectAuth --cli-unfold-argument  \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "BizToken": "CE661F1A-0F1E-45BD-BE13-34C05CEA7681",
        "Url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx2cca36a86d5035ae&redirect_uri=http%3A%2F%2Fopen.faceid.qq.com%2Fv1%2Fapi%2FgetCode%3FbizRedirect%3Dhttp%253A%252F%252Ffaceid.qq.com%252Fapi%252Fauth%252FgetOpenidAndSaveToken%253Ftoken%253DCE661F1A-0F1E-45BD-BE13-34C05CEA7681&response_type=code&scope=snsapi_base&state=&component_appid=wx9802ee81e68d6dee#wechat_redirect",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

