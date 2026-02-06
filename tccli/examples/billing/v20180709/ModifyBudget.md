**Example 1: 更新预算信息**



Input: 

```
tccli billing ModifyBudget --cli-unfold-argument  \
    --BudgetId 1963509727611473921 \
    --BudgetName API创建预算计划 \
    --CycleType DAY \
    --PeriodBegin 2025-01-01 \
    --PeriodEnd 2025-12-01 \
    --PlanType FIX \
    --BudgetQuota 1200 \
    --BillType BILL \
    --FeeType COST \
    --WarnJson.0.WarnType ACTUAL \
    --WarnJson.0.CalType PERCENTAGE \
    --WarnJson.0.ThresholdValue 100 \
    --BudgetNote 使用api创建预算信息 \
    --DimensionsRange.Business p_cvm \
    --WaveThresholdJson.0.WarnType ACTUAL \
    --WaveThresholdJson.0.Threshold 100 \
    --WaveThresholdJson.0.MetaType chain \
    --WaveThresholdJson.0.PeriodType day
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "BudgetId": "1963509727611473921",
            "UpdateTime": "2025-09-04 15:59:14"
        },
        "Message": "update success",
        "RequestId": "59e79af4-68cb-4bb3-9b18-194acf3952fe"
    }
}
```

