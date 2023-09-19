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
            "BandwidthPrice": null,
            "InstancePrice": {
                "OriginalPrice": 37.4,
                "DiscountPrice": 37.4,
                "UnitPrice": null,
                "ChargeUnit": null
            }
        },
        "RequestId": "2eff0c82-61a2-48e5-ae17-2037901dd17c"
    }
}
```

