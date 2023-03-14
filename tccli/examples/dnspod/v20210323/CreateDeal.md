**Example 1: DNSPod商品下单示例**

 DNSPod商品下单示例

Input: 

```
tccli dnspod CreateDeal --cli-unfold-argument  \
    --Domain 8988.ltd \
    --NewPackageType  \
    --GoodsNum 1 \
    --TimeSpan 12 \
    --AutoRenew 1 \
    --DealType 1 \
    --GoodsChildType DP_PLUS \
    --GoodsType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "896a1b04-814d-49d1-b404-42cc8d5b67f0",
        "DealList": [
            {
                "DealName": "20220519328000975112751",
                "DealId": "223011900"
            }
        ],
        "BigDealId": "20220519328000975112741"
    }
}
```

