**Example 1: 变配预付费资源询价**

使用该接口进行变配预付费资源询价，后付费资源变配询价需直接使用InquirePriceCreate接口

Input: 

```
tccli cynosdb InquirePriceModify --cli-unfold-argument  \
    --Cpu 0 \
    --Memory 0 \
    --StorageLimit 0 \
    --ClusterId abc \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "InstancePrice": {
            "TotalPrice": 0,
            "Discount": 0,
            "TotalPriceDiscount": 0,
            "UnitPrice": 0,
            "UnitPriceDiscount": 0,
            "ChargeUnit": "abc"
        },
        "StoragePrice": {
            "TotalPrice": 0,
            "Discount": 0,
            "TotalPriceDiscount": 0,
            "UnitPrice": 0,
            "UnitPriceDiscount": 0,
            "ChargeUnit": "abc"
        },
        "RequestId": "abc"
    }
}
```

