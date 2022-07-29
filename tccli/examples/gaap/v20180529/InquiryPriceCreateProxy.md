**Example 1: 创建加速通道询价**



Input: 

```
tccli gaap InquiryPriceCreateProxy --cli-unfold-argument  \
    --Concurrency 2 \
    --Bandwidth 10 \
    --RealServerRegion SouthChina \
    --AccessRegion EastChina
```

Output: 
```
{
    "Response": {
        "Cn2BandwidthPrice": 0.0,
        "Cn2BandwidthPriceWithDiscount": 0.0,
        "ProxyDailyPrice": 80.64,
        "FlowUnitPrice": 0.0,
        "Currency": "xx",
        "DiscountProxyDailyPrice": 56.84,
        "RequestId": "xx",
        "DiscountFlowUnitPrice": 0.0,
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            },
            {
                "BandwidthRange": [
                    2000,
                    0
                ],
                "BandwidthUnitPrice": 0.0,
                "DiscountBandwidthUnitPrice": 0.0
            }
        ]
    }
}
```

