**Example 1: 修改Budget属性**



Input: 

```
tccli clb ModifyBudgetAttributes --cli-unfold-argument  \
    --BudgetId budget-1a2b3c4d \
    --BudgetName production-budget-v2 \
    --BudgetConfigs.0.MaxBudget 200 \
    --BudgetConfigs.0.BudgetDuration 7d \
    --BudgetConfigs.1.MaxBudget 2000 \
    --BudgetConfigs.1.BudgetDuration 30d \
    --RateLimitConfig.TPM 200000 \
    --RateLimitConfig.RPM 120
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

