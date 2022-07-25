**Example 1: 续费集群询价**



Input: 

```
tccli cynosdb InquirePriceRenew --cli-unfold-argument  \
    --ClusterId xxx \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "Prices": [
            {
                "TotalPrice": 0,
                "TotalPriceDiscount": 0,
                "UnitPrice": 0,
                "Discount": 0.0,
                "UnitPriceDiscount": 0,
                "ChargeUnit": "xx"
            }
        ],
        "ClusterId": "xx",
        "RequestId": "xx",
        "InstanceIds": [
            "cynosdbmysql-ins-m3hy"
        ],
        "InstanceRealTotalPrice": 0,
        "StorageRealTotalPrice": 0
    }
}
```

