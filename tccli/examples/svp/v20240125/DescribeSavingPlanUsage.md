**Example 1: 查询节省计划使用率明细示例**



Input: 

```
tccli svp DescribeSavingPlanUsage --cli-unfold-argument  \
    --StartDate 2024-03-01 \
    --EndDate 2024-05-01 \
    --Offset 0 \
    --Limit 1 \
    --TimeInterval month
```

Output: 
```
{
    "Response": {
        "RequestId": "626b5af9-5c9e-4ffb-ab6c-ec370b75a355",
        "Total": 1,
        "Usages": [
            {
                "CostAmount": "600",
                "DeductAmount": "600",
                "DosageAmount": "0",
                "LossAmount": "0",
                "NetSavings": "-600",
                "PromiseAmount": "600",
                "Region": [
                    "15"
                ],
                "SpType": "svp_common",
                "Status": 1,
                "UtilizationRate": 100
            }
        ]
    }
}
```

