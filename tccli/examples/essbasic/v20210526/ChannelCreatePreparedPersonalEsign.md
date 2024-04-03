**Example 1: 参数UserName不能为空**

参数UserName不能为空

Input: 

```
tccli essbasic ChannelCreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --UserName  \
    --IdCardType abc \
    --IdCardNumber abc \
    --SealName abc \
    --SealImage abc \
    --SealImageCompress True \
    --Mobile abc \
    --EnableAutoSign True \
    --LicenseType 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "参数UserName不能为空"
        },
        "RequestId": "xxxx111xxxx"
    }
}
```

**Example 2: 参数IdCardNumber不能为空**

参数IdCardNumber不能为空

Input: 

```
tccli essbasic ChannelCreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --UserName abc \
    --IdCardType abc \
    --IdCardNumber  \
    --SealName abc \
    --SealImage abc \
    --SealImageCompress True \
    --Mobile abc \
    --EnableAutoSign True \
    --LicenseType 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "参数IdCardNumber不能为空"
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 通过准备好的个人印章图片创建印章**

通过准备好的个人印章图片创建印章

Input: 

```
tccli essbasic ChannelCreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --UserName 印章归属个人姓名 \
    --IdCardType  \
    --IdCardNumber 身份证件号码 \
    --SealImage 印章图片Base64 \
    --SealName 我的印章名称 \
    --Mobile 135*111 \
    --EnableAutoSign True
```

Output: 
```
{
    "Response": {
        "SealId": "abc",
        "RequestId": "abc"
    }
}
```

