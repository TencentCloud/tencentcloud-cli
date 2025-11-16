**Example 1: NAT网关询价**

查询NAT 1.0小型实例价格

Input: 

```
tccli vpc InquiryPriceNatGateway --cli-unfold-argument  \
    --MaxConcurrentConnection 1000000 \
    --NatProductVersion 1
```

Output: 
```
{
    "Response": {
        "InstancePrice": {
            "UnitPrice": 0.5,
            "ChargeUnit": "HOUR",
            "OriginalPrice": 0.5,
            "DiscountPrice": 0.5
        },
        "BandwidthPrice": {
            "UnitPrice": 0.8,
            "ChargeUnit": "GB",
            "OriginalPrice": 0.8,
            "DiscountPrice": 0.8
        },
        "CUPrice": null,
        "ScheduleServicePrice": null,
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.5,
                "ChargeUnit": "HOUR",
                "OriginalPrice": 0.5,
                "DiscountPrice": 0.5
            },
            "BandwidthPrice": {
                "UnitPrice": 0.8,
                "ChargeUnit": "GB",
                "OriginalPrice": 0.8,
                "DiscountPrice": 0.8
            }
        },
        "RequestId": "0389111e-9a1a-4b1a-ba29-92c781ddab43"
    }
}
```

