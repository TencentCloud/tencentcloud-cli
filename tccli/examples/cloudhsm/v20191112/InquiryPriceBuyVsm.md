**Example 1: 询价**



Input: 

```
tccli cloudhsm InquiryPriceBuyVsm --cli-unfold-argument  \
    --GoodsNum 1 \
    --PayMode 1 \
    --Currency CNY \
    --TimeSpan 1 \
    --TimeUnit m \
    --Type CREATE \
    --HsmType GHSM
```

Output: 
```
{
    "Response": {
        "GoodsNum": 1,
        "OriginalCost": 3500000,
        "RequestId": "cebaa3fa-2c01-4ebf-9158-30e9a96a179c",
        "TimeSpan": "1",
        "TimeUnit": "m",
        "TotalCost": 3500000
    }
}
```

