**Example 1: 包年包月实例调整配置询价**



Input: 

```
tccli cvm InquiryPriceResetInstancesType --cli-unfold-argument  \
    --InstanceType S5.16XLARGE256 \
    --InstanceIds ins-2zvpghhc
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
                "ChargeUnit": "xx",
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
                "ChargeUnit": "xx",
                "DiscountPriceThreeYear": 0.0,
                "DiscountPriceOneYear": 0.0
            }
        },
        "RequestId": "d9f36a23-7bc4-4f02-99c5-00b4a77431df"
    }
}
```

