**Example 1: 创建SIP通道示例**

创建SIP通道示例

Input: 

```
tccli ccc CreateSipTrunk --cli-unfold-argument  \
    --SipTrunk.Id 0 \
    --SipTrunk.Uin xx \
    --SipTrunk.AppId xx \
    --SipTrunk.Mode xx \
    --SipTrunk.CheckHealth True \
    --SipTrunk.ProviderId 0 \
    --SipTrunk.RegisterUserName xx \
    --SipTrunk.RegisterPassword xx \
    --SipTrunk.RegisterServer xx \
    --SipTrunk.RegisterServerPort 0 \
    --SipTrunk.RegisterOutboundProxy xx \
    --SipTrunk.RegisterOutboundProxyPort 0 \
    --SipTrunk.RegisterProto xx \
    --SipTrunk.RegisterFullName xx \
    --SipTrunk.RegisterExpires 0 \
    --SipTrunk.InboundCalleeFormat xx \
    --SipTrunk.InboundCalleeField xx \
    --SipTrunk.OutboundCallerFormat xx \
    --SipTrunk.State 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3651cda6-6501-4482-9f4e-8d0c9548a4db"
    }
}
```

