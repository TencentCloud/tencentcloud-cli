**Example 1: 创建Budget并关联实例**



Input: 

```
tccli clb CreateBudget --cli-unfold-argument  \
    --BudgetName production-budget \
    --BudgetConfigs.0.MaxBudget 100 \
    --BudgetConfigs.0.BudgetDuration 1d \
    --BudgetConfigs.1.MaxBudget 1000 \
    --BudgetConfigs.1.BudgetDuration 30d \
    --RateLimitConfig.TPM 100000 \
    --RateLimitConfig.RPM 60 \
    --Resources.0.Type ModelRouter \
    --Resources.0.ModelRouterId cmr-abc12345
```

Output: 
```
{
    "Response": {
        "BudgetId": "budget-1a2b3c4d",
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

