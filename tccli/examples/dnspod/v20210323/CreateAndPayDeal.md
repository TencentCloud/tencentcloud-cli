**Example 1: 续费专业版套餐**



Input: 

```
tccli dnspod CreateAndPayDeal --cli-unfold-argument  \
    --DealType 2 \
    --GoodsType 1 \
    --GoodsChildType DP_EXPERT \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --Domain qqqqq.asia \
    --TimeSpan 12
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260112880021950228161",
        "DealList": [
            {
                "DealId": "",
                "DealName": "20260112880021950228171",
                "ResourceId": ""
            }
        ],
        "RequestId": "2e90d5a6-9a4a-4b37-bbc1-3796a11c712d"
    }
}
```

