**Example 1: 预算金额历史记录**

成功示例

Input: 

```
tccli billing DescribeBudgetHistoryList --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
    --BudgetId 123
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "CountId": null,
            "Current": 1,
            "MaxLimit": null,
            "OptimizeCountSql": true,
            "Orders": [],
            "Pages": 8,
            "Records": [
                {
                    "BudgetDiff": "11111111.00",
                    "BudgetProgress": 0,
                    "BudgetQuota": "11111111.00",
                    "DateDesc": "2023-11",
                    "RealCost": "0.00",
                    "RemindTimes": 15
                }
            ],
            "SearchCount": true,
            "Size": 1,
            "Total": 8
        },
        "Message": null,
        "RequestId": "91811c20-2ebe-4f7f-9343-26029f964a76"
    }
}
```

