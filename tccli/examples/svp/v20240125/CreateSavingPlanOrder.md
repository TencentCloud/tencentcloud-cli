**Example 1: 节省计划下单实例**



Input: 

```
tccli svp CreateSavingPlanOrder --cli-unfold-argument  \
    --PromiseUseAmount 100 \
    --ZoneId 470004 \
    --TimeSpan 1 \
    --PrePayType 3 \
    --CommodityCode svp_common_CYq7cGNk3FaV \
    --TimeUnit y \
    --RegionId 47
```

Output: 
```
{
    "Response": {
        "RequestId": "04e854d9-f4b2-439e-b111-1660fc3e8ff9",
        "BigDealId": "20260318177135017340433"
    }
}
```

