**Example 1: 调整VPN网关带宽上限询价**

本接口（InquiryPriceResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限询价。

Input: 

```
tccli vpc InquiryPriceResetVpnGatewayInternetMaxBandwidth --cli-unfold-argument  \
    --VpnGatewayId vpngw-a4wta21x \
    --InternetMaxBandwidthOut 100
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 1717.86,
                "DiscountPrice": 1717.86,
                "UnitPrice": 0,
                "ChargeUnit": ""
            },
            "BandwidthPrice": {
                "OriginalPrice": 0,
                "DiscountPrice": 0,
                "UnitPrice": 0,
                "ChargeUnit": ""
            }
        },
        "RequestId": "e13643de-b578-42b0-8ad3-86b732067292"
    }
}
```

