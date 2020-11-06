**Example 1: 查询续费价格**



Input: 

```
tccli cds InquiryPriceDbauditInstance --cli-unfold-argument  \
    --TimeSpan 1 \
    --TimeUnit m \
    --InstanceVersion cdsaudit \
    --InquiryType renew \
    --ServiceRegion app-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7",
        "TotalPrice": "5000.00",
        "RealTotalCost": "5000.00"
    }
}
```

