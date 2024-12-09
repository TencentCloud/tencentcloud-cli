**Example 1: 包年包月询价输入**

包年包月询价时输入

Input: 

```
tccli vpc InquiryPriceCreateVpnGateway --cli-unfold-argument  \
    --InstanceChargeType PREPAID \
    --InstanceChargePrepaid.Period 1 \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 380,
                "DiscountPrice": 380,
                "UnitPrice": 0,
                "ChargeUnit": "none"
            },
            "BandwidthPrice": {
                "OriginalPrice": 0,
                "DiscountPrice": 0,
                "UnitPrice": 0,
                "ChargeUnit": "none"
            }
        },
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: 按量计费询价输入**

按量计费询价时输入

Input: 

```
tccli vpc InquiryPriceCreateVpnGateway --cli-unfold-argument  \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 0.48,
                "UnitPrice": 0.48,
                "DiscountPrice": 0.48,
                "ChargeUnit": "HOUR"
            },
            "BandwidthPrice": {
                "OriginalPrice": 0.8,
                "UnitPrice": 0.8,
                "DiscountPrice": 0.8,
                "ChargeUnit": "GB"
            }
        },
        "RequestId": "e87327cd-f8fa-4340-9959-58ebe8f11f6b"
    }
}
```

