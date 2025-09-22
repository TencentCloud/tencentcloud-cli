**Example 1: 创建预算项目**



Input: 

```
tccli billing CreateBudget --cli-unfold-argument  \
    --BudgetName testapi111 \
    --CycleType DAY \
    --PeriodBegin 2025-01-01 \
    --PeriodEnd 2025-12-01 \
    --PlanType FIX \
    --BudgetQuota 1000 \
    --BillType BILL \
    --FeeType COST \
    --WarnJson.0.WarnType ACTUAL \
    --WarnJson.0.CalType PERCENTAGE \
    --WarnJson.0.ThresholdValue 100 \
    --BudgetNote 使用api创建预算信息 \
    --DimensionsRange.Business None \
    --DimensionsRange.PayMode None \
    --DimensionsRange.ProductCodes None \
    --DimensionsRange.ComponentCodes None \
    --DimensionsRange.ZoneIds None \
    --DimensionsRange.RegionIds None \
    --DimensionsRange.ProjectIds None \
    --DimensionsRange.ActionTypes None \
    --DimensionsRange.ConsumptionTypes None \
    --DimensionsRange.Tags.0.TagKey None \
    --DimensionsRange.Tags.0.TagValue None \
    --DimensionsRange.PayerUins None \
    --DimensionsRange.OwnerUins None \
    --DimensionsRange.TreeNodeUniqKeys None \
    --WaveThresholdJson.0.WarnType None \
    --WaveThresholdJson.0.Threshold None \
    --WaveThresholdJson.0.MetaType None \
    --WaveThresholdJson.0.PeriodType None
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "BudgetId": "1963509727611474000",
            "UpdateTime": "2025-09-04 15:49:33"
        },
        "Message": "create success",
        "RequestId": "922dcc4b-55b2-401d-8eb8-9160117d07d4"
    }
}
```

