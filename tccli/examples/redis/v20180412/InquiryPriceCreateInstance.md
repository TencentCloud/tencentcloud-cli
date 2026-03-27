**Example 1: 示例**



Input: 

```
tccli redis InquiryPriceCreateInstance --cli-unfold-argument  \
    --TypeId 9 \
    --MemSize 4096 \
    --GoodsNum 3 \
    --Period 1 \
    --BillingMode 0 \
    --ZoneId 100002 \
    --RedisShardNum 1 \
    --RedisReplicasNum 1
```

Output: 
```
{
    "Response": {
        "AmountUnit": "pent",
        "Currency": "CNY",
        "HighPrecisionOriginalPrice": 280.0224,
        "HighPrecisionPrice": 280.0224,
        "OriginalPrice": 280,
        "Price": 280,
        "RequestId": "e250b8cf-6beb-462f-aa17-34b08ed6c164"
    }
}
```

