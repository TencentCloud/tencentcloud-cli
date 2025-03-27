**Example 1: 查询节省计划总览明细示例**



Input: 

```
tccli svp DescribeSavingPlanOverview --cli-unfold-argument  \
    --StartDate 2024-03-01 \
    --EndDate 2024-05-01 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Overviews": [
            {
                "EndTime": "2028-03-30 14:59:59",
                "PayAmount": "0",
                "Region": [
                    "33"
                ],
                "SavingAmount": "600",
                "SpType": "svp_common",
                "StartTime": "2023-03-30 14:00:00",
                "Status": 1,
                "PayType": 1
            }
        ],
        "RequestId": "aa36e003-786e-47aa-aefe-e717d749f964",
        "Total": 1
    }
}
```

