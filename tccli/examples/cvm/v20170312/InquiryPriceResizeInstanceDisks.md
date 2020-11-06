**Example 1: Querying the price for expanding the disk capacity of a pay-as-you-go instance**



Input: 

```
tccli cvm InquiryPriceResizeInstanceDisks --cli-unfold-argument  \
    --InstanceId ins-fd8spnmq \
    --DataDisks.0.DiskSize 100
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0.46,
                "ChargeUnit": "HOUR"
            }
        },
        "RequestId": "d63b4f53-335b-49fb-9aa1-1716bb9276f6"
    }
}
```

