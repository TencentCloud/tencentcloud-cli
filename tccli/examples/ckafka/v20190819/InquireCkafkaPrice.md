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
                "DetailPrices": {
                    "BandwidthPrice": {
                        "UnitPrice": 0,
                        "UnitPriceDiscount": 0,
                        "OriginalPrice": 0,
                        "DiscountPrice": 0,
                        "Discount": 100,
                        "GoodsNum": null,
                        "Currency": null,
                        "DiskType": null,
                        "TimeSpan": null,
                        "TimeUnit": null,
                        "Value": 0
                    },
                    "DiskPrice": {
                        "UnitPrice": 175,
                        "UnitPriceDiscount": 50.1,
                        "OriginalPrice": 175,
                        "DiscountPrice": 50.1,
                        "Discount": 28.3,
                        "GoodsNum": null,
                        "Currency": null,
                        "DiskType": "CLOUD_BASIC",
                        "TimeSpan": null,
                        "TimeUnit": null,
                        "Value": 500
                    },
                    "PartitionPrice": {
                        "UnitPrice": 0,
                        "UnitPriceDiscount": 0,
                        "OriginalPrice": 0,
                        "DiscountPrice": 0,
                        "Discount": 100,
                        "GoodsNum": null,
                        "Currency": null,
                        "DiskType": null,
                        "TimeSpan": null,
                        "TimeUnit": null,
                        "Value": 0
                    },
                    "TopicPrice": {
                        "UnitPrice": 0,
                        "UnitPriceDiscount": 0,
                        "OriginalPrice": 0,
                        "DiscountPrice": 0,
                        "Discount": 100,
                        "GoodsNum": null,
                        "Currency": null,
                        "DiskType": null,
                        "TimeSpan": null,
                        "TimeUnit": null,
                        "Value": 0
                    },
                    "InstanceTypePrice": {
                        "UnitPrice": 190,
                        "UnitPriceDiscount": 57.56,
                        "OriginalPrice": 190,
                        "DiscountPrice": 7.56,
                        "Discount": 30.3,
                        "GoodsNum": null,
                        "Currency": null,
                        "DiskType": null,
                        "TimeSpan": null,
                        "TimeUnit": null,
                        "Value": 1
                    }
                },
                "UnitPrice": 265,
                "UnitPriceDiscount": 647.7,
                "OriginalPrice": 265,
                "DiscountPrice": 67.67,
                "Discount": 29.92,
                "GoodsNum": 1,
                "Currency": "CNY",
                "DiskType": null,
                "TimeSpan": 1,
                "TimeUnit": "m",
                "Value": null
            },
            "PublicNetworkBandwidthPrice": null
        },
        "RequestId": "xxxx"
    }
}
```

