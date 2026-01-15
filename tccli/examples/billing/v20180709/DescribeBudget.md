**Example 1: 依据BudgetId获取预算信息**



Input: 

```
tccli billing DescribeBudget --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 1 \
    --BudgetId 1963509727611473921 \
    --BudgetName 预算信息001 \
    --BudgetStatus ACTIVE \
    --CycleTypes DAY
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "Current": 1,
            "Pages": 1,
            "Records": [
                {
                    "BillType": "BILL",
                    "BudgetId": "1963509727611473921",
                    "BudgetName": "API创建预算计划",
                    "BudgetNote": "使用api创建预算信息",
                    "BudgetProgress": "0.00",
                    "BudgetQuota": "1200",
                    "BudgetQuotaJson": null,
                    "BudgetSendInfoForm": [
                        {
                            "BudgetId": null,
                            "EndTime": "23:59:59",
                            "Id": null,
                            "NoticeWays": [
                                "EMAIL",
                                "SMS",
                                "SITE"
                            ],
                            "ReceiverIds": [],
                            "ReceiverType": "UIN",
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
                    "CreateTime": "2025-09-04 15:49:34",
                    "CurDateDesc": "2025-09-11",
                    "CycleType": "DAY",
                    "DefaultMode": 0,
                    "Dimensions": "COST",
                    "DimensionsRange": {
                        "ActionTypes": [
                            "postpay_deduct_d"
                        ],
                        "Business": [
                            "p_cvm"
                        ],
                        "ComponentCodes": [
                            "v_cpu"
                        ],
                        "ConsumptionTypes": [
                            "prepay_purchase"
                        ],
                        "OwnerUins": [
                            "909619400"
                        ],
                        "PayMode": [
                            "postPay"
                        ],
                        "PayerUins": [
                            "909619400"
                        ],
                        "ProductCodes": [
                            "sp_cvm"
                        ],
                        "ProjectIds": [
                            "0"
                        ],
                        "RegionIds": [
                            "47"
                        ],
                        "Tags": [
                            {
                                "TagKey": "部门",
                                "TagValue": [
                                    "部门123"
                                ]
                            }
                        ],
                        "TreeNodeUniqKeys": [
                            "[\"909610400-695dhs38c28\"]"
                        ],
                        "ZoneIds": [
                            "10001"
                        ]
                    },
                    "FeeType": "COST",
                    "ForecastCost": null,
                    "ForecastProgress": null,
                    "HasForecast": "1",
                    "MoneyStatus": 1,
                    "PayerUin": 909619400,
                    "PeriodBegin": "2025-01-01",
                    "PeriodEnd": "2025-12-01",
                    "PlanType": "FIX",
                    "RealCost": "0.00",
                    "RemindTimes": 0,
                    "TemplateType": null,
                    "UpdateTime": "2025-09-04 15:59:14",
                    "WarnJson": [
                        {
                            "CalType": "PERCENTAGE",
                            "ThresholdValue": "100",
                            "WarnType": "ACTUAL"
                        }
                    ],
                    "WaveThresholdJson": [
                        {
                            "MetaType": "chain",
                            "PeriodType": "day",
                            "Threshold": "100",
                            "WarnType": "ACTUAL"
                        }
                    ]
                }
            ],
            "Size": 1,
            "Total": 1
        },
        "Message": "query success",
        "RequestId": "9844721a-b6c5-4566-906c-41b88bf976f8"
    }
}
```

