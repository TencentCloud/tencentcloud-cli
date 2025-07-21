**Example 1: 创建SIP通道路由策略**



Input: 

```
tccli ccc CreateSipTrunkRoute --cli-unfold-argument  \
    --SipTrunkRoute.SipTrunkId 1 \
    --SipTrunkRoute.SdkAppId 1400000000 \
    --SipTrunkRoute.Direction out \
    --SipTrunkRoute.Prefix 1 \
    --SipTrunkRoute.Length 6
```

Output: 
```
{
    "Response": {
        "RequestId": "22590cbf-da98-4e81-a7bd-659140900268",
        "Id": 1
    }
}
```

