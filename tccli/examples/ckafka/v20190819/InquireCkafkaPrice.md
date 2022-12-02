**Example 1: Ckafka询价**



Input: 

```
tccli ckafka InquireCkafkaPrice --cli-unfold-argument  \
    --Partition 40 \
    --InstanceNum 1 \
    --InquiryDiskParam.DiskSize 500 \
    --InquiryDiskParam.DiskType SSD \
    --ZoneIds 100001 \
    --Topic 30 \
    --Bandwidth 40 \
    --MessageRetention 4 \
    --PublicNetworkParam.PublicNetworkChargeType BANDWIDTH_PREPAID \
    --PublicNetworkParam.PublicNetworkMonthly 10 \
    --InstanceChargeParam.InstanceChargePeriod 1 \
    --InstanceChargeParam.InstanceChargeType PREPAID \
    --InstanceType profession \
    --CategoryAction purchase
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstancePrice": {
                "DiscountPrice": 0.0,
                "GoodsNum": 0,
                "TimeSpan": 0,
                "DetailPrices": {
                    "TopicPrice": {
                        "DiscountPrice": 0.0,
                        "Value": 0,
                        "Discount": 0.0,
                        "OriginalPrice": 0.0,
                        "UnitPriceDiscount": 0.0,
                        "UnitPrice": 0.0
                    },
                    "PartitionPrice": {
                        "DiscountPrice": 0.0,
                        "Value": 0,
                        "Discount": 0.0,
                        "OriginalPrice": 0.0,
                        "UnitPriceDiscount": 0.0,
                        "UnitPrice": 0.0
                    },
                    "BandwidthPrice": {
                        "DiscountPrice": 0.0,
                        "Value": 0,
                        "Discount": 0.0,
                        "OriginalPrice": 0.0,
                        "UnitPriceDiscount": 0.0,
                        "UnitPrice": 0.0
                    }
                },
                "Discount": 0.0,
                "OriginalPrice": 0.0,
                "TimeUnit": "xx",
                "UnitPriceDiscount": 0.0,
                "Currency": "xx",
                "UnitPrice": 0.0
            },
            "PublicNetworkBandwidthPrice": {
                "DiscountPrice": 0.0,
                "GoodsNum": 0,
                "TimeSpan": 0,
                "DetailPrices": {},
                "Value": 0,
                "Discount": 0.0,
                "OriginalPrice": 0.0,
                "TimeUnit": "xx",
                "UnitPriceDiscount": 0.0,
                "Currency": "xx",
                "UnitPrice": 0.0
            }
        },
        "RequestId": "xx"
    }
}
```

