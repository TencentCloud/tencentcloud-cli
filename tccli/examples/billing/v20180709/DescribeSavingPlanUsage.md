**Example 1: 节省计划使用率查询示例**



Input: 

```
tccli billing DescribeSavingPlanUsage --cli-unfold-argument  \
    --StartDate 2023-01-10 \
    --EndDate 2023-10-20 \
    --Offset 0 \
    --Limit 10 \
    --TimeInterval day
```

Output: 
```
{
    "Response": {
        "RequestId": "b04c956e-b3f5-442d-89cf-8e380f3fd408",
        "Total": 1,
        "Usages": [
            {
                "CostAmount": "440",
                "DeductAmount": "440",
                "DosageAmount": "0",
                "LossAmount": "0",
                "NetSavings": "-440",
                "PromiseAmount": "440",
                "Region": [
                    "*"
                ],
                "SpType": "svp_common",
                "Status": 1,
                "UtilizationRate": 100
            }
        ]
    }
}
```

