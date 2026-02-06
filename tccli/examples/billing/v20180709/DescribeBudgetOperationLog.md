**Example 1: 根据BudgetId查询预算修改记录**



Input: 

```
tccli billing DescribeBudgetOperationLog --cli-unfold-argument  \
    --PageNo 1 \
    --PageSize 4 \
    --BudgetId 1967417069344325634
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
                    "Action": "ADD",
                    "BillDay": 20250915,
                    "BillMonth": "2025-09-01 00:00:00",
                    "BudgetId": "1967417069344325634",
                    "CreateTime": "2025-09-15 10:35:56",
                    "DiffValue": [
                        {
                            "After": "测试创建记录111222",
                            "Before": null,
                            "Property": "budgetName"
                        },
                        {
                            "After": "记录",
                            "Before": null,
                            "Property": "budgetNote"
                        },
                        {
                            "After": "BILL",
                            "Before": null,
                            "Property": "billType"
                        },
                        {
                            "After": "COST",
                            "Before": null,
                            "Property": "feeType"
                        },
                        {
                            "After": "DAY",
                            "Before": null,
                            "Property": "cycleType"
                        },
                        {
                            "After": "2025-01-01",
                            "Before": null,
                            "Property": "periodBegin"
                        },
                        {
                            "After": "2025-12-01",
                            "Before": null,
                            "Property": "periodEnd"
                        },
                        {
                            "After": "COST",
                            "Before": null,
                            "Property": "dimensions"
                        },
                        {
                            "After": "{\"business\":[\"p_cvm\"]}",
                            "Before": null,
                            "Property": "dimensionsRange"
                        },
                        {
                            "After": "FIX",
                            "Before": null,
                            "Property": "planType"
                        },
                        {
                            "After": "1000",
                            "Before": null,
                            "Property": "budgetQuota"
                        },
                        {
                            "After": "api修改",
                            "Before": null,
                            "Property": "operationChannel"
                        },
                        {
                            "After": "[{\"warnType\":\"ACTUAL\",\"threshold\":\"22\",\"metaType\":\"yoy\",\"periodType\":\"day\"}]",
                            "Before": "null",
                            "Property": "waveThresholdJson"
                        },
                        {
                            "After": "[{\"warnType\":\"ACTUAL\",\"calType\":\"ABS\",\"thresholdValue\":\"33\"}]",
                            "Before": "null",
                            "Property": "warnJson"
                        }
                    ],
                    "OperateUin": 103628347,
                    "OperationChannel": "api修改",
                    "OwnerUin": 103628347,
                    "PayerUin": 103628347,
                    "UpdateTime": "2025-09-15 10:35:56"
                }
            ],
            "Size": 4,
            "Total": 1
        },
        "Message": "query success",
        "RequestId": "4c1a5821-241d-44dc-b132-929bd648ddb3"
    }
}
```

