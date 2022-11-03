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
    --FlowId 字符串 \
    --Agent.ProxyAppId 字符串 \
    --Agent.ProxyOperator.OpenId 字符串 \
    --Agent.AppId 字符串 \
    --Agent.ProxyOrganizationOpenId 字符串 \
    --CancelMessage 字符串 \
    --CancelMessageFormat 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4b39b29f-xxxxxx308b91"
    }
}
```

