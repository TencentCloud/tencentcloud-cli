**Example 1: 修改SIP通道示例**

修改SIP通道示例

Input: 

```
tccli ccc ModifySipTrunk --cli-unfold-argument  \
    --SipTrunk.AllowIpList.0.Host 11.11.xx.xx \
    --SipTrunk.AllowIpList.0.Port 6001 \
    --SipTrunk.CheckHealth False \
    --SipTrunk.Id 1 \
    --SipTrunk.InboundCalleeField TO \
    --SipTrunk.InboundCalleeFormat NUMBER \
    --SipTrunk.Mode IP-ALLOW-LIST \
    --SipTrunk.Name xxxxxxx \
    --SipTrunk.OutboundCallerFormat NUMBER
```

Output: 
```
{
    "Response": {
        "RequestId": "3651cda6-6501-4482-9f4e-8d0c9548a4db"
    }
}
```

