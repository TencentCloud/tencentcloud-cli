**Example 1: 查询订单详情**



Input: 

```
tccli mongodb DescribeDBInstanceDeal --cli-unfold-argument  \
    --DealId 20200420111635
```

Output: 
```
{
    "Response": {
        "Action": "purchase",
        "DiscountPrice": 759.33,
        "OriginalPrice": 1116.67,
        "RequestId": "e79836e8-1864-45bf-aa63-0c7af31e7de5",
        "Status": 4
    }
}
```

