**Example 1: 预算基础信息1**

成功响应

Input: 

```
tccli billing DescribeBudgetInfoList --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1
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
            "Orders": [
                {
                    "Asc": false,
                    "Column": "id"
                }
            ],
            "Pages": 14,
            "Records": [
                {
                    "BillType": "BILL",
                    "DimensionsRangeJson": {
                        "ActionTypes": null,
                        "Business": null,
                        "ComponentCodes": null,
                        "ConsumptionTypes": null,
                        "PayMode": null,
                        "ProductCodes": null,
                        "ProjectIds": null,
                        "RegionIds": null,
                        "Tags": null,
                        "ZoneIds": null
                    },
                    "BudgetName": "8",
                    "BudgetNote": "",
                    "BudgetProgress": "34371.25",
                    "BudgetQuota": "16",
                    "BudgetQuotaJson": null,
                    "BudgetSendInfoForm": [
                        {
                            "BudgetId": null,
                            "EndTime": "23:59:59",
                            "Id": "ADoNrCzyuP",
                            "NoticeWays": [
                                "SITE"
                            ],
                            "ReceiverIds": [
                                16701087
                            ],
                            "ReceiverType": "USER",
                            "StartTime": "10:00:00",
                            "WeekDays": [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6,
                                7
                            ]
                        }
                    ],
                    "BudgetStatus": "ACTIVE",
                    "CreateTime": 1695255226000,
                    "CurDateDesc": "2023-11",
                    "CycleType": "MONTH",
                    "DefaultMode": 1,
                    "Dimensions": "COST",
                    "DimensionsRange": "",
                    "FeeType": "REAL_COST",
                    "Id": "1123",
                    "PayerUin": 999,
                    "PeriodBegin": "2023-09",
                    "PeriodEnd": "2024-09",
                    "PlanType": "FIX",
                    "RealCost": "5499.40",
                    "RemindTimes": 0,
                    "UpdateTime": 1695256278000,
                    "WarnJson": [
                        {
                            "CalType": "PERCENTAGE",
                            "ThresholdValue": "2",
                            "WarnType": "ACTUAL"
                        }
                    ],
                    "WaveThresholdJson": []
                }
            ],
            "SearchCount": true,
            "Size": 1,
            "Total": 14
        },
        "Message": null,
        "RequestId": "0c265872-e7a5-4eb6-a7eb-d49020a6441f"
    }
}
```

