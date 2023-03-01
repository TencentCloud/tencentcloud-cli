**Example 1: ChannelCancelMultiFlowSignQRCode**

ChannelCancelMultiFlowSignQRCode

Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --Operator.OpenId test \
    --Operator.ClientIp test \
    --Operator.CustomUserId test \
    --Operator.ProxyIp test \
    --Operator.Channel test \
    --QrCodeId test \
    --Agent.ProxyAppId test \
    --Agent.ProxyOrganizationId test \
    --Agent.ProxyOperator.OpenId test \
    --Agent.ProxyOperator.ClientIp test \
    --Agent.ProxyOperator.CustomUserId test \
    --Agent.ProxyOperator.ProxyIp test \
    --Agent.ProxyOperator.Channel test \
    --Agent.ProxyOrganizationOpenId test \
    --Agent.AppId test
```

Output: 
```
{
    "Response": {
        "RequestId": "id"
    }
}
```

