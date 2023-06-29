**Example 1: 查询促销活动**



Input: 

```
tccli tcss DescribePromotionActivity --cli-unfold-argument  \
    --ActiveID 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "MonthNum": 1,
                "ProfessionalDiscount": 1,
                "CoresCountLimit": 1,
                "ImageAuthorizationNum": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

