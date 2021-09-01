**Example 1: 调整VPN网关带宽上限询价**



Input: 

```
tccli vpc InquiryPriceResetVpnGatewayInternetMaxBandwidth --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-lazly92z \
    --InternetMaxBandwidthOut 10
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 460.27,
                "DiscountPrice": 460.27
            }
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

