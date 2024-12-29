**Example 1: 包年包月网关续费网关询价输入**

包年包月网关续费网关询价输入

Input: 

```
tccli vpc InquiryPriceRenewVpnGateway --cli-unfold-argument  \
    --VpnGatewayId vpngw-abcxa123z \
    --InstanceChargePrepaid.Period 1 \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 380.0,
                "DiscountPrice": 177.4,
                "UnitPrice": 0.0,
                "ChargeUnit": ""
            },
            "BandwidthPrice": {
                "OriginalPrice": 0.0,
                "DiscountPrice": 0.0,
                "UnitPrice": 0.0,
                "ChargeUnit": ""
            }
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

