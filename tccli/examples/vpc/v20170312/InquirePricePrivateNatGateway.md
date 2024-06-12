**Example 1: 私网网关询价**



Input: 

```
tccli vpc InquirePricePrivateNatGateway --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 1,
                "ChargeUnit": "HOUR",
                "OriginalPrice": 1,
                "DiscountPrice": 1
            },
            "CUPrice": {
                "UnitPrice": 1,
                "ChargeUnit": "CU",
                "OriginalPrice": 1,
                "DiscountPrice": 1
            }
        },
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

