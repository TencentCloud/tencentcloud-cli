**Example 1: 创建SIP通道示例**

创建SIP通道示例

Input: 

```
tccli ccc CreateSipTrunk --cli-unfold-argument  \
    --SipTrunk.InboundCalleeField TO \
    --SipTrunk.InboundCalleeFormat NUMBER \
    --SipTrunk.Mode REGISTER \
    --SipTrunk.Name 11 \
    --SipTrunk.OutboundCallerFormat NUMBER \
    --SipTrunk.RegisterExpires 3600 \
    --SipTrunk.RegisterOutboundProxy  \
    --SipTrunk.RegisterOutboundProxyPort 0 \
    --SipTrunk.RegisterPassword  \
    --SipTrunk.RegisterProto UDP \
    --SipTrunk.RegisterServer  \
    --SipTrunk.RegisterServerPort 5060 \
    --SipTrunk.RegisterUserName 
```

Output: 
```
{
    "Response": {
        "RequestId": "3651cda6-6501-4482-9f4e-8d0c9548a4db"
    }
}
```

