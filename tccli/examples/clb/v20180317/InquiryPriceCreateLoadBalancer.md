**Example 1: 查询创建预付费负载均衡价格**

查询创建预付费负载均衡价格

Input: 

```
tccli clb InquiryPriceCreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --LoadBalancerChargeType PREPAID \
    --GoodsNum 1 \
    --InternetAccessible.InternetChargeType BANDWIDTH_PREPAID \
    --InternetAccessible.InternetMaxBandwidthOut 1 \
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

**Example 2: 查询LB按量计费，网络按量计费的费用**

查询LB按量计费，网络按量计费的费用

Input: 

```
tccli clb InquiryPriceCreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --LoadBalancerChargeType POSTPAID \
    --InternetAccessible.InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.2,
                "UnitPriceDiscount": 0.0574,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 28.6951
            },
            "BandwidthPrice": {
                "UnitPrice": 0,
                "UnitPriceDiscount": 0,
                "ChargeUnit": "0",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 100
            },
            "LcuPrice": null
        },
        "RequestId": "8abe5fc0-690d-458a-a15e-7f7467968f5d"
    }
}
```

**Example 3: 查询创建LB按量计费，网络按带宽包计费**

查询创建LB按量计费，网络按带宽包计费

Input: 

```
tccli clb InquiryPriceCreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --LoadBalancerChargeType POSTPAID \
    --GoodsNum 1 \
    --InternetAccessible.InternetChargeType BANDWIDTH_PACKAGE \
    --InternetAccessible.BandwidthpkgSubType SINGLEISP
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.2,
                "UnitPriceDiscount": 0.0574,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 28.6951
            },
            "BandwidthPrice": {
                "UnitPrice": 0,
                "UnitPriceDiscount": 0,
                "ChargeUnit": "0",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 100
            },
            "LcuPrice": null
        },
        "RequestId": "4233547b-4201-4b65-a9f4-304dfcf2a6f0"
    }
}
```

**Example 4: 查询创建LB按量计费，网络按带宽计费的价格**

查询创建LB按量计费，网络按带宽计费的价格

Input: 

```
tccli clb InquiryPriceCreateLoadBalancer --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --LoadBalancerChargeType POSTPAID \
    --InternetAccessible.InternetChargeType BANDWIDTH_POSTPAID_BY_HOUR \
    --InternetAccessible.InternetMaxBandwidthOut 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.2,
                "UnitPriceDiscount": 0.0574,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 28.6951
            },
            "BandwidthPrice": {
                "UnitPrice": 0.04,
                "UnitPriceDiscount": 0.0137,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null,
                "Discount": 34.2927
            },
            "LcuPrice": null
        },
        "RequestId": "2c77d1f1-7cdb-49e8-b91c-da9aa1becb27"
    }
}
```

