**Example 1: 询价工作空间转换计费模式**



Input: 

```
tccli thpc InquirePriceModifyWorkspacesChargeType --cli-unfold-argument  \
    --SpaceIds wks-q8b3h7xt \
    --SpaceChargeType PREPAID \
    --SpaceChargePrepaid.Period 1 \
    --SpaceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "Price": {
            "SpacePrice": {
                "Discount": 100,
                "DiscountPrice": 146171.22999999998,
                "OriginalPrice": 146171.22999999998
            }
        },
        "RequestId": "faf63fd0-001b-4321-9f5e-99fa433bb83e"
    }
}
```

