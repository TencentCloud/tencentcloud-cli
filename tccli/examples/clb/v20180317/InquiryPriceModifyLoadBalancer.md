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
            "BandwidthPrice": null,
            "InstancePrice": {
                "OriginalPrice": 4494.57,
                "DiscountPrice": 4494.57,
                "UnitPrice": null,
                "ChargeUnit": null
            }
        },
        "RequestId": "4c588312-edeb-4ea0-b8a4-b3024d9b8043"
    }
}
```

