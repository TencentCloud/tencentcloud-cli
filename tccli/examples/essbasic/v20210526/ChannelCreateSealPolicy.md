**Example 1: 创建印章授权**

给指定用户下发印章授权

Input: 

```
tccli essbasic ChannelCreateSealPolicy --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --SealId yDRTZxxxxxJNR \
    --UserIds yDdzlxxxxxopk
```

Output: 
```
{
    "Response": {
        "UserIds": [
            "yDdzlxxxxxopk"
        ],
        "RequestId": "fdasfavdavxxxx"
    }
}
```

**Example 2: 授权时，缺少印章ID**

授权时，缺少印章ID

Input: 

```
tccli essbasic ChannelCreateSealPolicy --cli-unfold-argument  \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --SealId  \
    --UserIds abc \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Organization.OrganizationId abc \
    --Organization.Channel abc \
    --Organization.OrganizationOpenId abc \
    --Organization.ClientIp abc \
    --Organization.ProxyIp abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "缺失印章ID"
        },
        "RequestId": "abc"
    }
}
```

**Example 3: 授权时，找不到对应的 UserId**

授权时，找不到对应的 UserId

Input: 

```
tccli essbasic ChannelCreateSealPolicy --cli-unfold-argument  \
    --Agent.AppId abc \
    --Agent.ProxyOrganizationOpenId abc \
    --Agent.ProxyOperator.OpenId abc \
    --Agent.ProxyOperator.Channel abc \
    --Agent.ProxyOperator.CustomUserId abc \
    --Agent.ProxyOperator.ClientIp abc \
    --Agent.ProxyOperator.ProxyIp abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --SealId abc \
    --UserIds abc xxxid \
    --Operator.OpenId abc \
    --Operator.Channel abc \
    --Operator.CustomUserId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Organization.OrganizationId abc \
    --Organization.Channel abc \
    --Organization.OrganizationOpenId abc \
    --Organization.ClientIp abc \
    --Organization.ProxyIp abc
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "无效的授权用户Id"
        },
        "RequestId": "abc"
    }
}
```

