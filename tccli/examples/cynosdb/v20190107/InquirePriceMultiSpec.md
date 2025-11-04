**Example 1: 查询多规格价格**



Input: 

```
tccli cynosdb InquirePriceMultiSpec --cli-unfold-argument  \
    --Zone ap-guangzhou-4 \
    --InstancePayMode PREPAID \
    --StoragePayMode POSTPAID \
    --GoodsSpecs.0.GoodsNum 1 \
    --GoodsSpecs.0.Cpu 1 \
    --GoodsSpecs.0.Memory 1 \
    --GoodsSpecs.0.TimeSpan 1 \
    --GoodsSpecs.0.TimeUnit m
```

Output: 
```
{
    "Response": {
        "GoodsPrice": [
            {
                "GoodsSpec": {
                    "Ccu": 0,
                    "Cpu": 1,
                    "DeviceType": "",
                    "GoodsNum": 1,
                    "Memory": 1,
                    "StorageLimit": 0,
                    "TimeSpan": 1,
                    "TimeUnit": "m"
                },
                "InstancePrice": {
                    "ChargeUnit": "m",
                    "Discount": 100,
                    "TotalPrice": 6000,
                    "TotalPriceDiscount": 6000,
                    "UnitPrice": 0,
                    "UnitPriceDiscount": 0
                },
                "StoragePrice": {
                    "ChargeUnit": "",
                    "Discount": 0,
                    "TotalPrice": 0,
                    "TotalPriceDiscount": 0,
                    "UnitPrice": 0,
                    "UnitPriceDiscount": 0
                }
            }
        ],
        "RequestId": "b30bbeef-370b-4176c085"
    }
}
```

