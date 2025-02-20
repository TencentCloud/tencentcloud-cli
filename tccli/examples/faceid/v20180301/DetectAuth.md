**Example 1: 微信小程序获取BizToken成功示例**



Input: 

```
tccli faceid DetectAuth --cli-unfold-argument  \
    --RuleId 0 \
    --IdCard 11204416541220243X \
    --Name 韦小宝
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

**Example 2: H5获取BizToken成功示例**



Input: 

```
tccli faceid DetectAuth --cli-unfold-argument  \
    --RuleId 0 \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --Extra Orderid=f904f4cf75db4f8fdc4f942c7f7a \
    --RedirectUrl http://www.qq.com
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

**Example 3: 获取BizToken失败示例**



Input: 

```
tccli faceid DetectAuth --cli-unfold-argument  \
    --RuleId 999 \
    --IdCard 11204416541220243X \
    --Name 韦小宝
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.RuleIdNotExist",
            "Message": "RuleId不存在，请到人脸核身控制台申请。"
        },
        "RequestId": "e90c9abf-dcb3-4efa-97fc-5c4501b8182c"
    }
}
```

