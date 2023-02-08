**Example 1: 按量付费实例扩容磁盘询价**

按量付费实例扩容磁盘询价

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
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.46,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.0,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            },
            "BandwidthPrice": {
                "DiscountPrice": 0.0,
                "OriginalPriceThreeYear": 0.0,
                "DiscountOneYear": 0.0,
                "UnitPrice": 0.0,
                "UnitPriceThirdStep": 0.0,
                "OriginalPriceFiveYear": 0.0,
                "Discount": 0.0,
                "DiscountFiveYear": 0.0,
                "UnitPriceDiscountThirdStep": 0.0,
                "UnitPriceSecondStep": 0.0,
                "OriginalPrice": 0.0,
                "DiscountThreeYear": 0.0,
                "UnitPriceDiscountSecondStep": 0.0,
                "UnitPriceDiscount": 0.0,
                "DiscountPriceFiveYear": 0.0,
                "OriginalPriceOneYear": 0.0,
                "ChargeUnit": "HOUR",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            }
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

