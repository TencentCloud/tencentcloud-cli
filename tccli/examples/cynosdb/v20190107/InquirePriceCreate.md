**Example 1: 新购集群询价**



Input: 

```
tccli cynosdb InquirePriceCreate --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --GoodsNum 1 \
    --Cpu 1 \
    --Memory 1 \
    --StorageLimit 10 \
    --TimeSpan 1 \
    --TimeUnit m \
    --InstancePayMode POSTPAID \
    --StoragePayMode POSTPAID
```

Output: 
```
{
    "Response": {
        "InstancePrice": {
            "ChargeUnit": "",
            "Discount": 100,
            "TotalPrice": 200,
            "TotalPriceDiscount": 200,
            "UnitPrice": 0,
            "UnitPriceDiscount": 0
        },
        "RequestId": "123-123bcde-1243",
        "StoragePrice": {
            "ChargeUnit": "GB*h",
            "Discount": 100,
            "TotalPrice": 0,
            "TotalPriceDiscount": 0,
            "UnitPrice": 350,
            "UnitPriceDiscount": 350
        }
    }
}
```

