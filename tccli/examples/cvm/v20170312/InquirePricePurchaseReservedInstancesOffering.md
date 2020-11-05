**Example 1: Querying the price of reserved instance offerings**



Input: 

```
tccli cvm InquirePricePurchaseReservedInstancesOffering --cli-unfold-argument  \
    --InstanceCount 2\
    --ReservedInstancesOfferingId noew0342-324f-f3ab-9uut-wrlnth53dcee
```

Output: 
```
{
    "Response": {
        "OriginalFixedPrice": 100.99,
        "DiscountFixedPrice": 100.99,
        "OriginalUsagePrice": 1.99,
        "DiscountUsagePrice": 1.99,
        "RequestId": "b333ddb8-4aed-4def-a0d9-617043c2614e"
    }
}
```

