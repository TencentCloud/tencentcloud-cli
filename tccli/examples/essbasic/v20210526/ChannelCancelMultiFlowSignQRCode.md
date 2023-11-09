**Example 1: 取消一码多扫流程签署二维码**

取消一码多扫流程签署二维码

Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --QrCodeId yDSLZUUckpooi1ltUxCsD3RSTG9BEWhR \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "RequestId": "dfc69a6f-7738-45f3-a238-99e0e89bc91a"
    }
}
```

**Example 2: 取消一码多扫流程签署二维码-已失效**

废除一码多扫流程签署二维码，若二维码已经失效，则返回操作失败。

Input: 

```
tccli essbasic ChannelCancelMultiFlowSignQRCode --cli-unfold-argument  \
    --QrCodeId yDSLZUUckpooi1ltUxCsD3RSTG9BEWhR \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.QrInvalid",
            "Message": "签署二维码不可用，请检查后重试。"
        },
        "RequestId": "dfc69a6f-7738-45f3-a238-99e0e89bc91a"
    }
}
```

