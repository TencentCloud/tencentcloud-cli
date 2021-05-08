**Example 1: 查询一个镜像的价格**



Input: 

```
tccli lighthouse InquirePriceCreateBlueprint --cli-unfold-argument  \
    --BlueprintCount 5
```

Output: 
```
{
    "Response": {
        "BlueprintPrice": {
            "OriginalBlueprintPrice": 0.008,
            "OriginalPrice": 0.04,
            "Discount": 100,
            "DiscountPrice": 0.04
        },
        "RequestId": "afde8c49-eb92-4545-a464-ebe788a249c4"
    }
}
```

