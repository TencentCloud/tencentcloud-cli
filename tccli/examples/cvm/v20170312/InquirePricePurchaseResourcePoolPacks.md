**Example 1: 创建实例资源池预扣包询价**

创建实例资源池预扣包询价

Input: 

```
tccli cvm InquirePricePurchaseResourcePoolPacks --cli-unfold-argument  \
    --Zone ap-guangzhou-7 \
    --InstanceType S9.8XLARGE64 \
    --InstanceCount 1 \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "ChargeUnit": "HOUR",
            "Discount": 100,
            "UnitPrice": 1.36,
            "UnitPriceDiscount": 1.36
        },
        "RequestId": "0ea883b1-0fc2-4e9b-afc7-d1a28d216083"
    }
}
```

