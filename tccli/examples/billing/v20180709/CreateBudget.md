**Example 1: 创建预算项目**



Input: 

```
tccli billing CreateBudget --cli-unfold-argument  \
    --BudgetName API创建预算 \
    --CycleType DAY \
    --PeriodBegin 2025-01-01 \
    --PeriodEnd 2026-12-01 \
    --PlanType FIX \
    --BudgetQuota 1000 \
    --BillType BILL \
    --FeeType COST \
    --WarnJson.0.WarnType ACTUAL \
    --WarnJson.0.CalType PERCENTAGE \
    --WarnJson.0.ThresholdValue 100 \
    --BudgetNote 使用api创建预算信息 \
    --DimensionsRange.Business p_cvm \
    --DimensionsRange.PayMode postPay \
    --DimensionsRange.ProductCodes sp_cvm \
    --DimensionsRange.ComponentCodes v_cpu \
    --DimensionsRange.ZoneIds 10001 \
    --DimensionsRange.RegionIds 47 \
    --DimensionsRange.ProjectIds 0 \
    --DimensionsRange.ActionTypes postpay_deduct_d \
    --DimensionsRange.ConsumptionTypes prepay_purchase \
    --DimensionsRange.Tags.0.TagKey 业务部门 \
    --DimensionsRange.Tags.0.TagValue 部门123 \
    --DimensionsRange.PayerUins 909619400 \
    --DimensionsRange.OwnerUins 909619400 \
    --DimensionsRange.TreeNodeUniqKeys 909619400-6872sdw23 \
    --WaveThresholdJson.0.WarnType ACTUAL \
    --WaveThresholdJson.0.Threshold 10 \
    --WaveThresholdJson.0.MetaType chain \
    --WaveThresholdJson.0.PeriodType day
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

