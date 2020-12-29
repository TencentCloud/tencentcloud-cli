**Example 1: 创建加速通道询价**



Input: 

```
tccli gaap InquiryPriceCreateProxy --cli-unfold-argument  \
    --AccessRegion EastChina \
    --RealServerRegion SouthChina \
    --Bandwidth 10 \
    --Concurrency 2
```

Output: 
```
{
    "Response": {
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

