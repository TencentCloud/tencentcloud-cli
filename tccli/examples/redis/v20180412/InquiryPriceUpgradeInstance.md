**Example 1: 示例**



Input: 

```
tccli redis InquiryPriceUpgradeInstance --cli-unfold-argument  \
    --InstanceId crs-i7flj4ir \
    --MemSize 1024 \
    --RedisShardNum 1 \
    --RedisReplicasNum 1
```

Output: 
```
{
    "Response": {
        "AmountUnit": "pent",
        "Currency": "CNY",
        "HighPrecisionOriginalPrice": 21.111112,
        "HighPrecisionPrice": 21.111112,
        "OriginalPrice": 21,
        "Price": 21,
        "RequestId": "6b36919f-29e6-43cf-bf94-24af6b0c8c93"
    }
}
```

