**Example 1: Querying monthly subscription prices**



Input: 

```
tccli vpc InquiryPriceCreateVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12 \
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
                "DiscountPrice": 380
            }
        },
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

**Example 2: Querying pay-as-you-go prices**



Input: 

```
tccli vpc InquiryPriceCreateVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12 \
    --InstanceChargeType POSTPAID_BY_HOUR \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.48,
                "ChargeUnit": "HOUR"
            },
            "BandwidthPrice": {
                "UnitPrice": 0.8,
                "ChargeUnit": "GB"
            }
        },
        "RequestId": "e87327cd-f8fa-4340-9959-58ebe8f11f6b"
    }
}
```

