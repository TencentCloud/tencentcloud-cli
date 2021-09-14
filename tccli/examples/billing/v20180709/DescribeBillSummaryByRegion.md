**Example 1: 获取按地域汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByRegion --cli-unfold-argument  \
    --BeginTime 2018-11 \
    --EndTime 2018-11
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "RegionId": "0",
                "RealTotalCost": "198.03",
                "TotalCost": "-",
                "CashPayAmount": "199.82",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "-1.79",
                "RealTotalCostRatio": "88.09",
                "BillMonth": "2021-01",
                "RegionName": "其他"
            },
            {
                "RegionId": "19",
                "RealTotalCost": "26.78",
                "TotalCost": "-",
                "CashPayAmount": "6.30",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "20.48",
                "RealTotalCostRatio": "11.91",
                "BillMonth": "2021-01",
                "RegionName": "西南地区（重庆）"
            },
            {
                "RegionId": "1",
                "RealTotalCost": "0.00",
                "TotalCost": "-",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2021-01",
                "RegionName": "华南地区（广州）"
            },
            {
                "RegionId": "8",
                "RealTotalCost": "0.00",
                "TotalCost": "-",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2021-01",
                "RegionName": "华北地区（北京）"
            },
            {
                "RegionId": "4",
                "RealTotalCost": "0.00",
                "TotalCost": "-",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2021-01",
                "RegionName": "华东地区（上海）"
            }
        ],
        "RequestId": "0db6d3bf-d9b2-4c64-9424-3675a55ac792"
    }
}
```

