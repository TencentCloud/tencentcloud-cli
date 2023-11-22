**Example 1: 结算计划下单**



Input: 

```
tccli billing CreateSavingPlanOrder --cli-unfold-argument  \
    --RegionId 47 \
    --ZoneId 470004 \
    --PrePayType 1 \
    --SpecifyEffectTime 2023-10-21 00:00:00 \
    --TimeSpan 1 \
    --TimeUnit y \
    --CommodityCode svp_common_CYq7cGNk3FaV \
    --PromiseUseAmount 10000 \
    --ClientToken sp-856f5555-8064-43e9-8b7e-d04c5a9d6a9a,856f5555806443e98b7ed04c5a9d6a9a
```

Output: 
```
{
    "Response": {
        "BigDealId": "20231020400000764159521",
        "RequestId": "7525ef6b-ac63-4fa6-9bd4-d8c3c8b96220"
    }
}
```

