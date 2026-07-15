**Example 1: 续费CDH实例询价**

续费CDH实例询价

Input: 

```
tccli cvm InquiryPriceRenewHosts --cli-unfold-argument  \
    --HostIds host-ey16rkyg \
    --HostChargePrepaid.Period 1 \
    --HostChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "Price": {
            "HostPrice": {
                "OriginalPrice": 37050,
                "DiscountPrice": 37050
            }
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

