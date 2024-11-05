**Example 1: 续费集群询价**



Input: 

```
tccli cynosdb InquirePriceRenew --cli-unfold-argument  \
    --ClusterId cynosdbmysql-prao75jd \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "ClusterId": "cynosdbmysql-prao75jd",
        "InstanceIds": [
            "cynosdbmysql-ins-1rh1dodd"
        ],
        "InstanceRealTotalPrice": 15686,
        "Prices": [
            {
                "ChargeUnit": "m",
                "Discount": 48.058876,
                "TotalPrice": 32640,
                "TotalPriceDiscount": 15686,
                "UnitPrice": 0,
                "UnitPriceDiscount": 0
            }
        ],
        "RequestId": "bbcbe6f9-f8fc-40e6-ba0b-00301b48c8ff",
        "StorageRealTotalPrice": 0
    }
}
```

