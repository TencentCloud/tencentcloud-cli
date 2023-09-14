**Example 1: 包年包月实例调整配置询价**



Input: 

```
tccli cvm InquiryPriceResetInstancesType --cli-unfold-argument  \
    --InstanceType S5.16XLARGE256 \
    --InstanceIds ins-xmf2ac34
```

Output: 
```
{
    "Response": {
        "Price": {
            "InstancePrice": {
                "UnitPrice": 0,
                "ChargeUnit": "abc",
                "OriginalPrice": 0,
                "DiscountPrice": 0,
                "Discount": 0,
                "UnitPriceDiscount": 0,
                "UnitPriceSecondStep": 0,
                "UnitPriceDiscountSecondStep": 0,
                "UnitPriceThirdStep": 0,
                "UnitPriceDiscountThirdStep": 0,
                "OriginalPriceThreeYear": 0,
                "DiscountPriceThreeYear": 0,
                "DiscountThreeYear": 0,
                "OriginalPriceFiveYear": 0,
                "DiscountPriceFiveYear": 0,
                "DiscountFiveYear": 0,
                "OriginalPriceOneYear": 0,
                "DiscountPriceOneYear": 0,
                "DiscountOneYear": 0
            },
            "BandwidthPrice": {
                "UnitPrice": 0,
                "ChargeUnit": "abc",
                "OriginalPrice": 0,
                "DiscountPrice": 0,
                "Discount": 0,
                "UnitPriceDiscount": 0,
                "UnitPriceSecondStep": 0,
                "UnitPriceDiscountSecondStep": 0,
                "UnitPriceThirdStep": 0,
                "UnitPriceDiscountThirdStep": 0,
                "OriginalPriceThreeYear": 0,
                "DiscountPriceThreeYear": 0,
                "DiscountThreeYear": 0,
                "OriginalPriceFiveYear": 0,
                "DiscountPriceFiveYear": 0,
                "DiscountFiveYear": 0,
                "OriginalPriceOneYear": 0,
                "DiscountPriceOneYear": 0,
                "DiscountOneYear": 0
            }
        },
        "RequestId": "abc"
    }
}
```

