**Example 1: Querying renewal price of an instance**



Input: 

```
tccli mongodb InquirePriceRenewDBInstances --cli-unfold-argument  \
    --InstanceIds cmgo-8oij5631\
    --InstanceChargePrepaid.Period 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "DiscountPrice": 455.6,
            "OriginalPrice": 670,
            "UnitPrice": 0
        },
        "RequestId": "d08f2a0f-4a69-451e-8ddb-753340d5fb34"
    }
}
```

