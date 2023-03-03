**Example 1: 生成默认的控制台链接**

生成默认的控制台链接

Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 子客企业名称 \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId testx \
    --Agent.AppId test
```

Output: 
```
{
    "Response": {
        "ConsoleUrl": "https://xxx.xxxx.tencent.com/?channel=PROXYCHANNEL&expiredTime=1631712951&code=123456asdfghjk&menuStatus=ENABLE",
        "IsActivated": false,
        "ProxyOperatorIsVerified": false,
        "RequestId": "s16221xxx14775648"
    }
}
```

**Example 2: 生成到模板详情的控制台链接**

生成到模板详情的控制台链接

Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 子客企业名称 \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test \
    --Module TEMPLATE \
    --ModuleId test \
    --MenuStatus ENABLE
```

Output: 
```
{
    "Response": {
        "ConsoleUrl": "https://xxx.xxxx.tencent.com/template-preview?channel=PROXYCHANNEL&expiredTime=1631712951&code=123456asdfghjk&templateId=yDxlzxxxoTxQfVnyxs&menuStatus=ENABLE",
        "IsActivated": false,
        "ProxyOperatorIsVerified": false,
        "RequestId": "s16221xxx14775648"
    }
}
```

