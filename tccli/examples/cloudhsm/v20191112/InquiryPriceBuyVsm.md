**Example 1: 询价**



Input: 

```
tccli cloudhsm InquiryPriceBuyVsm --cli-unfold-argument  \
    --PayMode 1 \
    --TimeUnit y \
    --Type CREATE \
    --GoodsNum 1 \
    --TimeSpan 1
```

Output: 
```
{
    "Response": {
        "TotalCost": 2000.0,
        "GoodsNum": 1,
        "TimeSpan": 1,
        "TimeUnit": "y",
        "OriginalCost": 2000.0,
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239"
    }
}
```

