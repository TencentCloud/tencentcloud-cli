**Example 1: 活动商品下单预扣减商品配额**



Input: 

```
tccli opc TryDeductActivityGoodsQuota --cli-unfold-argument  \
    --DealUin 100013140416 \
    --TradeID 79e48cb6-e3ad-4a77-990f-65929144934f \
    --GoodsParamList.0.GoodsID 47372 \
    --GoodsParamList.0.GoodsDealParam {} \
    --GoodsParamList.0.GoodsNum 1
```

Output: 
```
{
    "Response": {
        "ActiveFlowList": [
            31576
        ],
        "RequestId": "075de7b2-4a76-4abf-86da-95f200607d33"
    }
}
```

