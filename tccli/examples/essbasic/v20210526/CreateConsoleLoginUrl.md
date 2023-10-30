**Example 1: 生成默认的控制台链接**

生成默认的控制台链接

Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 典子谦示例企业 \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH
```

Output: 
```
{
    "Response": {
        "ConsoleUrl": "https://xxx.xxxx.tencent.com/?channel=PROXYCHANNEL&expiredTime=1631712951&code=123456asdfghjk&menuStatus=ENABLE",
        "IsActivated": false,
        "ProxyOperatorIsVerified": false,
        "RequestId": "s16221***14775648"
    }
}
```

**Example 2: 生成到模板详情的控制台链接**

生成到模板详情的控制台链接

Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 典子谦示例企业 \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.AppId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --Module TEMPLATE \
    --ModuleId yDwFdUUckpsvet4jUEn0aFRxtu5TdalM \
    --MenuStatus ENABLE
```

Output: 
```
{
    "Response": {
        "ConsoleUrl": "https://es*.ap*.tencent.com/template-preview?channel=PROXYCHANNEL&expiredTime=1631712951&code=123456asdfghjk&templateId=yDxlzxxxoTxQfVnyxs&menuStatus=ENABLE",
        "IsActivated": false,
        "ProxyOperatorIsVerified": false,
        "RequestId": "s16221***14775648"
    }
}
```

