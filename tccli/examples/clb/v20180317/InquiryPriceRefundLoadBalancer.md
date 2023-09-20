**Example 1: 负载均衡退费询价**

负载均衡退费询价

Input: 

```
tccli clb InquiryPriceRefundLoadBalancer --cli-unfold-argument  \
    --LoadBalancerId lb-56hl5sy2
```

Output: 
```
{
    "Response": {
        "Price": {
            "BandwidthPrice": null,
            "InstancePrice": {
                "UnitPrice": null,
                "ChargeUnit": null,
                "OriginalPrice": 79.02,
                "DiscountPrice": null
            }
        },
        "RequestId": "06cdb8b7-1d26-4195-9d41-f3fc861d9530"
    }
}
```

