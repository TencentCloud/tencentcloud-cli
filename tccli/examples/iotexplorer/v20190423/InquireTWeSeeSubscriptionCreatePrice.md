**Example 1: 查询开通 1 个月视频理解的价格**



Input: 

```
tccli iotexplorer InquireTWeSeeSubscriptionCreatePrice --cli-unfold-argument  \
    --ServiceType VID_COMP \
    --ServiceTier BASIC \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "1200",
        "OriginalPrice": "2000",
        "RequestId": "bb29e90b-c495-42a5-9184-378d42abfe4f"
    }
}
```

