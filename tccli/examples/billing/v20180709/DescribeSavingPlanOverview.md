**Example 1: 查询节省计划明细示例**



Input: 

```
tccli billing DescribeSavingPlanOverview --cli-unfold-argument  \
    --StartDate 2023-01-10 \
    --EndDate 2023-10-20 \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Overviews": [
            {
                "BuyTime": "2023-10-23 01:39:39",
                "EndTime": "2023-11-23 01:59:59",
                "PayAmount": "730",
                "PayType": 1,
                "Region": [
                    "1"
                ],
                "SavingAmount": "0",
                "SpType": "svp_common",
                "StartTime": "2023-10-23 01:00:00",
                "Status": 2
            },
            {
                "BuyTime": "2023-10-21 01:40:24",
                "EndTime": "2023-11-21 01:59:59",
                "PayAmount": "730",
                "PayType": 1,
                "Region": [
                    "1"
                ],
                "SavingAmount": "0",
                "SpType": "svp_common",
                "StartTime": "2023-10-21 01:00:00",
                "Status": 2
            }
        ],
        "RequestId": "402f99cc-6ccf-49f5-a79e-ebd7ca680ef3",
        "Total": 64
    }
}
```

