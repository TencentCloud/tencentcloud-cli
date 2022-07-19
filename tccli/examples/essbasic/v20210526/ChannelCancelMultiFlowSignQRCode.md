**Example 1: ChannelCancelMultiFlowSignQRCode**



Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.OpenId xx \
    --Operator.ClientIp xx \
    --Operator.CustomUserId xx \
    --Operator.ProxyIp xx \
    --Operator.Channel xx \
    --QrCodeId xx \
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
        "RequestId": "xx"
    }
}
```

