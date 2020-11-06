**Example 1: 按量付费实例扩容磁盘询价**



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

