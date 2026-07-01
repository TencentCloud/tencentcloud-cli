**Example 1: DNSPod商品下单示例-套餐续费**

套餐续费-尊享版套餐续费

Input: 

```
tccli dnspod CreateAndPayDeal --cli-unfold-argument  \
    --DealType 2 \
    --GoodsType 1 \
    --GoodsChildType DP_ULTRA \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --Domain *****.com \
    --TimeSpan 12
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260112880021950185241",
        "DealList": [
            {
                "DealId": "",
                "DealName": "20260112880021950185251",
                "ResourceId": ""
            }
        ],
        "RequestId": "b69f8d4d-8f4d-485f-b83d-e21ffd644ae0"
    }
}
```

**Example 2: DNSPod商品下单示例-套餐升级**

套餐升级-专业版升级为尊享版

Input: 

```
tccli dnspod CreateAndPayDeal --cli-unfold-argument  \
    --DealType 3 \
    --GoodsType 1 \
    --GoodsChildType DP_PLUS \
    --GoodsNum 1 \
    --AutoRenew 1 \
    --Domain *****.com \
    --NewPackageType DP_ULTRA \
    --ClientToken 4395743543re
```

Output: 
```
{
    "Response": {
        "BigDealId": "20260112880021950233691",
        "DealList": [
            {
                "DealId": "",
                "DealName": "20260112880021950258141",
                "ResourceId": ""
            }
        ],
        "RequestId": "ad5ce959-44ff-4c79-a6b7-146f28e46533"
    }
}
```

