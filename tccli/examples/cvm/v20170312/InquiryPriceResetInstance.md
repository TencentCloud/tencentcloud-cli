**Example 1: Querying the price of a pay-as-you-go instance with a new configuration**



Input: 

```
tccli cvm InquiryPriceResetInstance --cli-unfold-argument  \
    --InstanceId ins-fd8spnmq
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.66,
                "ChargeUnit": "HOUR",
                "UnitPriceDiscount": 0.66,
                "Discount": 100
            }
        },
        "RequestId": "56d68b92-7004-4716-b3bf-3c2c231035c9"
    }
}
```

