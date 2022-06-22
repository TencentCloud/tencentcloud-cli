**Example 1: 查询实例扩容价格**



Input: 

```
tccli postgres InquiryPriceUpgradeDBInstance --cli-unfold-argument  \
    --Storage 500 \
    --DBInstanceId postgres-6fego161 \
    --Memory 4
```

Output: 
```
{
    "Response": {
        "Price": 1300,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "OriginalPrice": 1300,
        "Currency": "CNY"
    }
}
```

