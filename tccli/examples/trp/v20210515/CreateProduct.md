**Example 1: 新建商品**



Input: 

```
tccli trp CreateProduct --cli-unfold-argument  \
    --Remark 商品备注 \
    --Name 商品名称 \
    --Specification 100ml \
    --Logo https://xxx.xxx.com/logo.png \
    --MerchantId eqdmnz7020bmtvi9 \
    --MerchantName demo
```

Output: 
```
{
    "Response": {
        "ProductId": "tz6jpscwky41u23o9b",
        "RequestId": "5ef09b37-e0c0-49b2-89ad-3345916d7abb"
    }
}
```

