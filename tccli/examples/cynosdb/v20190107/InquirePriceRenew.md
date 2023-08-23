**Example 1: 续费集群询价**



Input: 

```
tccli cynosdb InquirePriceRenew --cli-unfold-argument  \
    --ClusterId cynosdbmysql-aqws \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "ClusterId": "cynosdbmysql-qswe",
        "InstanceIds": [
            "cynosdbmysql-ins-poiu"
        ],
        "Prices": [
            {
                "TotalPrice": 0,
                "Discount": 0,
                "TotalPriceDiscount": 0,
                "UnitPrice": 0,
                "UnitPriceDiscount": 0,
                "ChargeUnit": "abc"
            }
        ],
        "InstanceRealTotalPrice": 0,
        "StorageRealTotalPrice": 0,
        "RequestId": "abc"
    }
}
```

