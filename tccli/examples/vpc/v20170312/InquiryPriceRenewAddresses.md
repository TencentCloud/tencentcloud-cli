**Example 1: 包月带宽计费模式EIP续费询价**



Input: 

```
tccli vpc InquiryPriceRenewAddresses --cli-unfold-argument  \
    --AddressIds eip-iu4ml5pp \
    --AddressChargePrepaid.Period 12
```

Output: 
```
{
    "Response": {
        "Price": {
            "AddressPrice": {
                "OriginalPrice": 240,
                "DiscountPrice": 240
            }
        },
        "RequestId": "84658acc-bdb9-4a3e-a37a-84a2e0c14e44"
    }
}
```

