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
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

