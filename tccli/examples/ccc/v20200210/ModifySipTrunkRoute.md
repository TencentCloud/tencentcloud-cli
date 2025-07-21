**Example 1: 修改SIP通道内线路由策略**



Input: 

```
tccli ccc ModifySipTrunkRoute --cli-unfold-argument  \
    --SipTrunkRoute.Id 1 \
    --SipTrunkRoute.SdkAppId 140000000 \
    --SipTrunkRoute.Direction out \
    --SipTrunkRoute.Prefix 2 \
    --SipTrunkRoute.Length 6
```

Output: 
```
{
    "Response": {
        "RequestId": "22590cbf-da98-4e81-a7bd-659140900268"
    }
}
```

