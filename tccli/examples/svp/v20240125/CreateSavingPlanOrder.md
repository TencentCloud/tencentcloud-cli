**Example 1: 节省计划下单**



Input: 

```
tccli svp CreateSavingPlanOrder --cli-unfold-argument  \
    --RegionId 47 \
    --ZoneId 470004 \
    --PrePayType 1 \
    --SpecifyEffectTime 2023-10-21 00:00:00 \
    --TimeSpan 1 \
    --TimeUnit y \
    --CommodityCode svp_common_CYq7cGNk3FaV \
    --PromiseUseAmount 10000 \
    --ClientToken sp-856f5555
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

