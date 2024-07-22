**Example 1: 创建加速通道询价**

创建加速通道询价

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
        "ProxyDailyPrice": 0,
        "BandwidthUnitPrice": [
            {
                "BandwidthRange": [
                    0
                ],
                "BandwidthUnitPrice": 0,
                "DiscountBandwidthUnitPrice": 0
            }
        ],
        "DiscountProxyDailyPrice": 0,
        "Currency": "abc",
        "FlowUnitPrice": 0,
        "DiscountFlowUnitPrice": 0,
        "Cn2BandwidthPrice": 0,
        "Cn2BandwidthPriceWithDiscount": 0,
        "RequestId": "abc"
    }
}
```

