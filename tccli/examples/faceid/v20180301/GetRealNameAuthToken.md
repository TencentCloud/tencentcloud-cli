**Example 1: 微信实名认证鉴权**



Input: 

```
tccli faceid GetRealNameAuthToken --cli-unfold-argument  \
    --Name XXX \
    --IDCard XXX \
    --CallbackURL https://xxxxx
```

Output: 
```
{
    "Response": {
        "AuthToken": "4ad3f260-44f8-0000-88ca-5254001a1560",
        "RedirectURL": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=xxx&redirect_uri=xxx&response_type=code&scope=snsapi_base&state=&component_appid=xxx#wechat_redirect",
        "RequestId": "97a8fcbf-9998-4e95-ac38-6f1a2308a021"
    }
}
```

