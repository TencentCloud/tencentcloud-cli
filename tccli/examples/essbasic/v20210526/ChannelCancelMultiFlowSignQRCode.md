**Example 1: ChannelCancelMultiFlowSignQRCode**

ChannelCancelMultiFlowSignQRCode

Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --QrCodeId test \
    --Agent.ProxyAppId test \
    --Agent.ProxyOperator.OpenId test \
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

