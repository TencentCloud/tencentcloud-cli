**Example 1: 续费实例询价**

续费实例询价

Input: 

```
tccli cvm InquiryPriceRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_MANUAL_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds ins-2zvpghhc
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "OriginalPrice": 120.0,
                "DiscountPrice": 1.2
            }
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
```

**Example 2: 查询单个实例费用信息**

查询单个实例费用信息

Input: 

```
tccli cvm InquiryPriceRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds ins-xlsl6f2h
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {},
            "BandwidthPrice": {}
        },
        "RequestId": "e2e81b08-d747-455e-b27a-aecc5acafdba"
    }
}
```

