**Example 1: ChannelCancelMultiFlowSignQRCode**

ChannelCancelMultiFlowSignQRCode

Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --QrCodeId test \
    --Agent.ProxyOperator.OpenId 自定义 \
    --Agent.ProxyOrganizationOpenId 自定义 \
    --Agent.AppId yDxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "1c75e86d-xxxxxxxxxx6f330a05e"
    }
}
```

