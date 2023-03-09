**Example 1: 获取创建印章的嵌入WEB链接**

获取创建印章的嵌入WEB链接

Input: 

```
tccli essbasic ChannelCreateEmbedWebUrl --cli-unfold-argument  \
    --Operator.OpenId  \
    --Operator.Channel CHANNEL \
    --Operator.CustomUserId 1 \
    --Operator.ClientIp 1.1.1.1 \
    --Operator.ProxyIp 0.0.0.0 \
    --BusinessId  \
    --EmbedType CREATE_SEAL \
    --Agent.AppId 1 \
    --Agent.ProxyOrganizationOpenId 1 \
    --Agent.ProxyOperator.OpenId 1 \
    --Agent.ProxyOperator.Channel 1 \
    --Agent.ProxyOperator.CustomUserId 1 \
    --Agent.ProxyOperator.ClientIp 1 \
    --Agent.ProxyOperator.ProxyIp 1 \
    --Agent.ProxyAppId 1 \
    --Agent.ProxyOrganizationId 1
```

Output: 
```
{
    "Response": {
        "WebUrl": "https://test.ess.com/seal-create?embed=1&code=testcode&channel=PROXYCHANNEL",
        "RequestId": "2"
    }
}
```

