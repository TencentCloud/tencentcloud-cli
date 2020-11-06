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
        "DiscountProxyDailyPrice": 56.84,
        "Currency": "CNY",
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0,
                    20
                ],
                "BandwidthUnitPrice": 130
            },
            {
                "BandwidthRange": [
                    20,
                    100
                ],
                "BandwidthUnitPrice": 90
            },
            {
                "BandwidthRange": [
                    100,
                    500
                ],
                "BandwidthUnitPrice": 70
            },
            {
                "BandwidthRange": [
                    500,
                    2000
                ],
                "BandwidthUnitPrice": 60
            },
            {
                "BandwidthRange": [
                    2000,
                    -1
                ],
                "BandwidthUnitPrice": 50
            }
        ],
        "RequestId": "81370460-5826-4c6f-a864-9b825a4a04b9"
    }
}
```

