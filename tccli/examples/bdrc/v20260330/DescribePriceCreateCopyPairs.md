**Example 1: 查询创建CVM复制对的后付费价格**

查询创建3个CVM复制对的价格，盘容量分别为50GB、100GB、200GB

Input: 

```
tccli bdrc DescribePriceCreateCopyPairs --cli-unfold-argument  \
    --DataCapacities 50 100 200
```

Output: 
```
{
    "Response": {
        "CopyPairPrices": [
            {
                "UnitPrice": 0.23,
                "UnitPriceHigh": "0.225",
                "UnitPriceDiscount": 0.23,
                "UnitPriceDiscountHigh": "0.225",
                "Discount": 100,
                "ChargeUnit": "HOUR",
                "DetailPrices": [
                    {
                        "PriceName": "InstanceDataCapacity",
                        "PriceTitle": "容灾CVM实例数据量",
                        "UnitPrice": 0.03,
                        "UnitPriceDiscount": 0.03,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    },
                    {
                        "PriceName": "InstanceCount",
                        "PriceTitle": "容灾CVM实例数",
                        "UnitPrice": 0.2,
                        "UnitPriceDiscount": 0.2,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    }
                ]
            },
            {
                "UnitPrice": 0.26,
                "UnitPriceHigh": "0.255",
                "UnitPriceDiscount": 0.26,
                "UnitPriceDiscountHigh": "0.255",
                "Discount": 100,
                "ChargeUnit": "HOUR",
                "DetailPrices": [
                    {
                        "PriceName": "InstanceDataCapacity",
                        "PriceTitle": "容灾CVM实例数据量",
                        "UnitPrice": 0.06,
                        "UnitPriceDiscount": 0.06,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    },
                    {
                        "PriceName": "InstanceCount",
                        "PriceTitle": "容灾CVM实例数",
                        "UnitPrice": 0.2,
                        "UnitPriceDiscount": 0.2,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    }
                ]
            },
            {
                "UnitPrice": 0.32,
                "UnitPriceHigh": "0.315",
                "UnitPriceDiscount": 0.32,
                "UnitPriceDiscountHigh": "0.315",
                "Discount": 100,
                "ChargeUnit": "HOUR",
                "DetailPrices": [
                    {
                        "PriceName": "InstanceDataCapacity",
                        "PriceTitle": "容灾CVM实例数据量",
                        "UnitPrice": 0.12,
                        "UnitPriceDiscount": 0.12,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    },
                    {
                        "PriceName": "InstanceCount",
                        "PriceTitle": "容灾CVM实例数",
                        "UnitPrice": 0.2,
                        "UnitPriceDiscount": 0.2,
                        "Discount": 100,
                        "ChargeUnit": "HOUR"
                    }
                ]
            }
        ],
        "RequestId": "7b946c85-57bd-4dc9-b509-899e2c9a736d"
    }
}
```

