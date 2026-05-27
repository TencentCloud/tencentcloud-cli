**Example 1: DescribeCustomerOwnCostExplorerSummary**

用于子客查询成本分析数据

Input: 

```
tccli intlpartnersmgt DescribeCustomerOwnCostExplorerSummary --cli-unfold-argument  \
    --Dimension Default \
    --FeeType originalCost \
    --BillType 1 \
    --StartTime 2024-09-01 00:00:00 \
    --EndTime 2024-09-12 23:59:59 \
    --PeriodType day \
    --Page 1 \
    --PageSize 10 \
    --Filter.BusinessIn p_cbs \
    --Filter.ProductIn sp_cbs_premium \
    --Filter.RegionIn 1 \
    --Filter.ActionTypeIn pre_purchase \
    --Filter.PayModeIn prePay \
    --Filter.ProjectIn default \
    --Filter.PayerUinIn 8000******** \
    --Filter.ZoneIn 100002 \
    --Filter.OwnerUinIn 80000******* \
    --Filter.ResourceIn disk-f*******
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "Code": "",
                "ItemDetail": [
                    {
                        "Cost": "0.7",
                        "Period": "2024-09-09"
                    }
                ],
                "Name": "default",
                "SumCost": "0.7"
            }
        ],
        "DimensionName": "Default",
        "TotalDetail": {
            "PeriodItemDetail": [
                {
                    "Cost": "0.7",
                    "Period": "2024-09-09"
                }
            ],
            "SumCost": "0.7",
            "TotalCount": 1
        },
        "RequestId": "af9d9375-bc8e-4bf5-ad4c-7a83033f4fc3"
    }
}
```

