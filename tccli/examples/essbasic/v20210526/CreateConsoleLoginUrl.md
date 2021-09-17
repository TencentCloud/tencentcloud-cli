**Example 1: 生成控制台链接**



Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 渠道侧企业名称 \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e \
    --Module TEMPLATE \
    --ModuleId yDxlzUyKQDlWe6UuO4zjE8oTxQfVnyxs
```

Output: 
```
{
    "Response": {
        "ConsoleUrl": "https://xxx.xxxx.tencent.com/template-preview?channel=PROXYCHANNEL&expiredTime=1631712951&code=123456asdfghjk&templateId=yDxlzUyKQDlWe6UuO4zjE8oTxQfVnyxs",
        "IsActivated": false,
        "RequestId": "s16221xxx14775648"
    }
}
```

