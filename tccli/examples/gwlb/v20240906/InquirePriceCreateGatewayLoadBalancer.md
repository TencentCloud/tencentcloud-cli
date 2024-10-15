**Example 1: 创建网关负载均衡询价**



Input: 

```
tccli gwlb InquirePriceCreateGatewayLoadBalancer --cli-unfold-argument  \
    --GoodsNum 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "ChargeUnit": "HOUR",
                "Discount": 100,
                "DiscountPrice": null,
                "OriginalPrice": null,
                "UnitPrice": 0.098,
                "UnitPriceDiscount": 0.098
            },
            "LcuPrice": {
                "ChargeUnit": "HOUR",
                "Discount": 100,
                "DiscountPrice": null,
                "OriginalPrice": null,
                "UnitPrice": 0.028,
                "UnitPriceDiscount": 0.028
            }
        },
        "RequestId": "9938ffa4-795a-4eb7-90be-3960b0659a6e"
    }
}
```

