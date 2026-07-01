**Example 1: 查询Budget列表**



Input: 

```
tccli clb DescribeBudgets --cli-unfold-argument  \
    --BudgetIds budget-1a2b3c4d \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "BudgetSet": [
            {
                "BudgetId": "budget-1a2b3c4d",
                "BudgetName": "production-budget",
                "BudgetConfigs": [
                    {
                        "MaxBudget": 100,
                        "BudgetDuration": "7d"
                    }
                ],
                "RateLimitConfig": {
                    "TPM": 100000,
                    "RPM": 60
                },
                "Status": "Active",
                "CreatedTime": "2026-04-14T12:00:00+08:00",
                "ModifiedTime": "2026-04-14T12:10:00+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

