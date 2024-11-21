**Example 1: 获取E证通Token成功示例**



Input: 

```
tccli faceid GetEidToken --cli-unfold-argument  \
    --MerchantId 0NSJ240626160443125212
```

Output: 
```
{
    "Response": {
        "EidToken": "CE661F1A-0F1E-45BD-BE13-34C05CEA7681",
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a",
        "Url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxa50a8ac37958245f53&redirect_uri=https%3A%2F%2Feid.faceid.qq.com%2Fapi%2Fv1%2FGetOpenId%3Ftoken%3DCE3661F1A-0F1E-45BD-BE113-34C05CEA7681&response_type=code&scope=snsapi_base&state=&component_appid=wx9802ee81e68d6dee#wechat_redirect"
    }
}
```

**Example 2: 获取E证通Token失败示例**



Input: 

```
tccli faceid GetEidToken --cli-unfold-argument  \
    --MerchantId 0NSJ240615216044312521
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.UnregisteredEid",
            "Message": "该用户未注册E证通，请先注册并跟公安库核验。"
        },
        "RequestId": "dc401e69-32bf-4002-83ca-3a12f62f2e4b"
    }
}
```

