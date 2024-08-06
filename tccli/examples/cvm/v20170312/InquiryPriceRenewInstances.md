**Example 1: 续费实例询价**

续费实例询价，时长为一个月

Input: 

```
tccli cvm InquiryPriceRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds ins-2zvpghhc
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 120,
                "DiscountPrice": 1.2
            }
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
```

