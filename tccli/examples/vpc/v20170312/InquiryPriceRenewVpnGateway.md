**Example 1: 包年包月网关续费网关询价输入**



Input: 

```
tccli vpc InquiryPriceRenewVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12 \
    --VpnGatewayId vpngw-lazly92z \
    --InstanceChargePrepaid.Period 2
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 760.0,
                "DiscountPrice": 760.0
            }
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

