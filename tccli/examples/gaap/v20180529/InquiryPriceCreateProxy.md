**Example 1: 创建加速通道询价**

创建加速通道询价

Input: 

```
tccli gaap InquiryPriceCreateProxy --cli-unfold-argument  \
    --Concurrent 2 \
    --Bandwidth 10 \
    --RealServerRegion Shanghai \
    --AccessRegion Guangzhou \
    --IPAddressVersion IPv4 \
    --NetworkType normal
```

Output: 
```
{
    "Response": {
        "ProxyDailyPrice": 80.64,
        "DiscountProxyDailyPrice": 80.64,
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 130,
                "DiscountBandwidthUnitPrice": 130
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 90,
                "DiscountBandwidthUnitPrice": 90
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 70,
                "DiscountBandwidthUnitPrice": 70
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 60,
                "DiscountBandwidthUnitPrice": 60
            },
            {
                "BandwidthRange": [
                    2000,
                    -1
                ],
                "BandwidthUnitPrice": 50,
                "DiscountBandwidthUnitPrice": 50
            }
        ],
        "Currency": "CNY",
        "RequestId": "d04ffc2a-5c92-455c-b1b1-1d4e460a63e2",
        "FlowUnitPrice": null,
        "DiscountFlowUnitPrice": null,
        "Cn2BandwidthPrice": 0,
        "Cn2BandwidthPriceWithDiscount": 0
    }
}
```

