**Example 1: 查询某个预付费负载均衡的价格的续费价格**

查询某个预付费负载均衡的价格的续费价格

Input: 

```
tccli clb InquiryPriceRenewLoadBalancer --cli-unfold-argument  \
    --LoadBalancerId lb-dr0mo6w4 \
    --LoadBalancerChargePrepaid.Period 1
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

