**Example 1: 查询LB按量计费，网络按量计费的费用**

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
                "UnitPrice": 0.02,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "BandwidthPrice": {
                "UnitPrice": 0.8,
                "ChargeUnit": "GB",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "LcuPrice": null
        },
        "RequestId": "f4953b5c-990c-49fa-9937-7aebef241d42"
    }
}
```

**Example 2: 查询创建LB按量计费，网络按带宽计费的价格**

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
                "UnitPrice": 0.02,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "BandwidthPrice": {
                "UnitPrice": 0.04,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "LcuPrice": null
        },
        "RequestId": "835f9cd8-6af1-4ac6-8fc3-2a9f900b7fff"
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
                "UnitPrice": 0.02,
                "ChargeUnit": "HOUR",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "BandwidthPrice": {
                "UnitPrice": 48,
                "ChargeUnit": "Mbps/MONTH",
                "OriginalPrice": null,
                "DiscountPrice": null
            },
            "LcuPrice": null
        },
        "RequestId": "19a2e45d-ed96-4f60-a954-99a4d41752f3"
    }
}
```

**Example 4: 查询创建预付费负载均衡价格**

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
            "BandwidthPrice": null,
            "InstancePrice": {
                "OriginalPrice": 37.4,
                "DiscountPrice": 37.4,
                "UnitPrice": null,
                "ChargeUnit": null
            },
            "LcuPrice": null
        },
        "RequestId": "52f22ea7-3592-4ff0-9d63-a5cc14b79859"
    }
}
```

