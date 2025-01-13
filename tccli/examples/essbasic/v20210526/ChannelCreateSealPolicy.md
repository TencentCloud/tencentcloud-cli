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
    --Agent.AppId jsdk812kxkdfjks***k88123123 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --Agent.ProxyOperator.Channel CHANNEL \
    --Agent.ProxyOperator.CustomUserId zhangsan \
    --Agent.ProxyOperator.ClientIp 1.2.3.4 \
    --Agent.ProxyOperator.ProxyIp 1.2.3.4 \
    --Agent.ProxyAppId yDRS4UUgygqdcj56UuO4zjExBQcOiB68 \
    --Agent.ProxyOrganizationId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --SealId  \
    --UserIds yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Operator.OpenId test_openid \
    --Operator.Channel CHANNEL \
    --Operator.CustomUserId zhangsan \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.ProxyIp 8.8.8.8 \
    --Organization.OrganizationId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Organization.Channel CHANNEL \
    --Organization.OrganizationOpenId org_dianziqian \
    --Organization.ClientIp 1.2.3.4 \
    --Organization.ProxyIp 8.8.8.8
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "缺失印章ID"
        },
        "RequestId": "s1111999868619888777"
    }
}
```

**Example 3: 授权时，找不到对应的 UserId**

授权时，找不到对应的 UserId

Input: 

```
tccli essbasic ChannelCreateSealPolicy --cli-unfold-argument  \
    --Agent.AppId jsdk812kxkdfjks***k88123123 \
    --Agent.ProxyOrganizationOpenId test_org_openid \
    --Agent.ProxyOperator.OpenId test_openid \
    --Agent.ProxyOperator.Channel CHANNEL \
    --Agent.ProxyOperator.CustomUserId zhangsan \
    --Agent.ProxyOperator.ClientIp 1.2.3.4 \
    --Agent.ProxyOperator.ProxyIp 1.2.3.4 \
    --Agent.ProxyAppId yDRS4UUgygqdcj56UuO4zjExBQcOiB68 \
    --Agent.ProxyOrganizationId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --SealId  \
    --UserIds yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Operator.OpenId test_openid \
    --Operator.Channel CHANNEL \
    --Operator.CustomUserId zhangsan \
    --Operator.ClientIp 8.8.8.8 \
    --Operator.ProxyIp 8.8.8.8 \
    --Organization.OrganizationId yDxbWUyKQDxgXVUuO4zjEB8mxCcDjAyF \
    --Organization.Channel CHANNEL \
    --Organization.OrganizationOpenId org_dianziqian \
    --Organization.ClientIp 1.2.3.4 \
    --Organization.ProxyIp 8.8.8.8
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.ParamError",
            "Message": "无效的授权用户Id"
        },
        "RequestId": "s1111999868619888777"
    }
}
```

