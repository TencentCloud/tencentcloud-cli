**Example 1: Querying the price for renewing a monthly subscription gateway**



Input: 

```
tccli vpc InquiryPriceRenewVpnGateway --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpnGatewayId vpngw-lazly92z\
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

