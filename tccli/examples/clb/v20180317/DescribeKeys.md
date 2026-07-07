**Example 1: 查询模型路由实例下的Key列表**



Input: 

```
tccli clb DescribeKeys --cli-unfold-argument  \
    --ModelRouterId cmr-pm53f9c3 \
    --KeyIds vkey-lboa0hhh \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Keys": [
            {
                "KeyId": "vkey-lboa0hhh",
                "KeyName": "prod-key",
                "Key": "sk-***BRk",
                "Status": "Active",
                "RateLimitConfig": {
                    "TPM": 50000,
                    "RPM": 30,
                    "MaxParallelRequest": 10
                },
                "BudgetId": "budget-1a2b3c4d",
                "BudgetName": "production-budget",
                "CreditUsageSet": [
                    {
                        "BudgetDuration": "1d",
                        "Limit": 100,
                        "Used": 12.34,
                        "BudgetResetAt": "2026-04-17T00:00:00+08:00"
                    },
                    {
                        "BudgetDuration": "30d",
                        "Limit": 1000,
                        "Used": 123.45,
                        "BudgetResetAt": "2026-05-01T00:00:00+08:00"
                    }
                ],
                "Tags": [],
                "CreatedTime": "2026-04-07T14:45:32+08:00",
                "ModifiedTime": "2026-04-07T22:45:31+08:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

