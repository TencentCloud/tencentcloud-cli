**Example 1: 查询调整数据库配置价格**



Input: 

```
tccli mongodb InquirePriceModifyDBInstanceSpec --cli-unfold-argument  \
    --InstanceId cmgo-8oij5631 \
    --Memory 8 \
    --Volume 200
```

Output: 
```
{
    "Response": {
        "Price": {
            "DiscountPrice": 449.36,
            "OriginalPrice": 660.82,
            "UnitPrice": 0
        },
        "RequestId": "ac618a97-5a29-4003-8489-fd8a1e1cc8e9"
    }
}
```

