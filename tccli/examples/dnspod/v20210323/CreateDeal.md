**Example 1: DNSPod商品下单示例-套餐升级**

套餐升级-专业版升级为企业版

Input: 

```
tccli dnspod CreateDeal --cli-unfold-argument  \
    --Domain dnspod.cn \
    --NewPackageType DP_EXPERT \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --DealType 3 \
    --GoodsChildType DP_PLUS \
    --GoodsType 1
```

Output: 
```
{
    "Response": {
        "BigDealId": "20251208409118512305171",
        "DealList": [
            {
                "DealId": "2902231877",
                "DealName": "20251208409118512305181"
            }
        ],
        "RequestId": "1595ce14-89d0-42c3-b7e0-7670f6945181"
    }
}
```

**Example 2: DNSPod商品下单示例-套餐新购**

套餐新购

Input: 

```
tccli dnspod CreateDeal --cli-unfold-argument  \
    --Domain dnspod.cn \
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

