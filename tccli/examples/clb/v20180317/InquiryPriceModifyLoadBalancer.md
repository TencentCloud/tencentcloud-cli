**Example 1: 查询负载均衡修改带宽的费用**

查询负载均衡修改带宽的费用

Input: 

```
tccli clb InquiryPriceModifyLoadBalancer --cli-unfold-argument  \
    --LoadBalancerId lb-dr0mo6w4 \
    --InternetAccessible.InternetChargeType BANDWIDTH_PREPAID \
    --InternetAccessible.InternetMaxBandwidthOut 20
```

Output: 
```
{
    "Response": {
        "Price": {
            "BandwidthPrice": {
                "ChargeUnit": null,
                "Discount": 34.7841,
                "DiscountPrice": 8,
                "OriginalPrice": 23,
                "UnitPrice": null,
                "UnitPriceDiscount": null
            },
            "InstancePrice": {
                "ChargeUnit": null,
                "Discount": 28.9198,
                "DiscountPrice": 41.64,
                "OriginalPrice": 144,
                "UnitPrice": null,
                "UnitPriceDiscount": null
            },
            "LcuPrice": null
        },
        "RequestId": "52f22ea7-3592-4ff0-9d63-a5cc14b79859"
    }
}
```

