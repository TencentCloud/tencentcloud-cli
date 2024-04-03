**Example 1: 生成默认的控制台登录链接**

如果<b>典子谦示例企业的员工张三已经完成了认证和加入企业</b>，  此时给典子谦示例企业的员工张三生成登录的PC控制台的链接

典子谦示例企业的定义标识为：org_dianziqian
员工张三定义员工标识为：n9527


Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 典子谦示例企业 \
    --ProxyOperatorName 张三 \
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

**Example 2: 生成默认的控制台认证链接**

如果<b>典子谦示例企业的员工张三还没有认证</b>，  此时给典子谦示例企业的员工张三生成企业认证和个人认证的PC链接

典子谦示例企业的定义标识为：org_dianziqian
员工张三定义员工标识为：n9527


Input: 

```
tccli essbasic CreateConsoleLoginUrl --cli-unfold-argument  \
    --ProxyOrganizationName 典子谦示例企业 \
    --ProxyOperatorName 张三 \
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

**Example 3: 生成到模板详情的控制台链接**

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

