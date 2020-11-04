**Example 1: 续费实例询价**



Input: 

```
tccli cvm InquiryPriceRenewInstances --cli-unfold-argument  \
    --InstanceIds ins-2zvpghhc\
    --InstanceChargePrepaid.Period 1\
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": "120.00",
                "DiscountPrice": "1.20"
            }
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
```

