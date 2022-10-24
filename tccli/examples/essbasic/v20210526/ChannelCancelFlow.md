**Example 1: 渠道版撤销签署流程**



Input: 

```
tccli essbasic ChannelCancelFlow --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xx \
    --Operator.Channel xx \
    --FlowId xx \
    --CancelMessage xx \
    --Agent.ProxyAppId xx \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId xx \
    --Agent.ProxyOperator.ClientIp xx \
    --Agent.ProxyOperator.CustomUserId xx \
    --Agent.ProxyOperator.ProxyIp xx \
    --Agent.ProxyOperator.Channel xx \
    --Agent.ProxyOrganizationOpenId xx \
    --Agent.AppId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "s16221xxxx12775546"
    }
}
```

**Example 2: 测试**



Input: 

```
tccli essbasic ChannelCancelFlow --cli-unfold-argument  \
    --Operator.OpenId 字符串 \
    --Operator.ClientIp 字符串 \
    --Operator.CustomUserId 字符串 \
    --Operator.ProxyIp 字符串 \
    --Operator.Channel 字符串 \
    --FlowId 字符串 \
    --Agent.ProxyAppId 字符串 \
    --Agent.ProxyOperator.OpenId 字符串 \
    --Agent.ProxyOperator.ClientIp 字符串 \
    --Agent.ProxyOperator.CustomUserId 字符串 \
    --Agent.ProxyOperator.ProxyIp 字符串 \
    --Agent.ProxyOperator.Channel 字符串 \
    --Agent.AppId 字符串 \
    --Agent.ProxyOrganizationOpenId 字符串 \
    --Agent.ProxyOrganizationId 字符串 \
    --CancelMessage 字符串 \
    --CancelMessageFormat 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4b39b29f-aca1-419d-9120-cd5b3e308b91"
    }
}
```

