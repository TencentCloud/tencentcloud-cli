**Example 1: 变配预付费资源询价**

使用该接口进行变配预付费资源询价，后付费资源变配询价需直接使用InquirePriceCreate接口

Input: 

```
tccli cynosdb InquirePriceModify --cli-unfold-argument  \
    --Cpu 0 \
    --Memory 0 \
    --StorageLimit 0 \
    --ClusterId cynosdbmysql-j9i41hdd \
    --InstanceId cynosdbmysql-ins-4vdtei11
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
            "ChargeUnit": ""
        },
        "StoragePrice": {
            "TotalPrice": 0,
            "Discount": 0,
            "TotalPriceDiscount": 0,
            "UnitPrice": 0,
            "UnitPriceDiscount": 0,
            "ChargeUnit": "GB*h"
        },
        "RequestId": "8f291dbc-3840-40f9-aa39-841437c247fb"
    }
}
```

