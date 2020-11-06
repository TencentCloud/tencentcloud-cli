**Example 1: Getting cost distribution over different regions**



Input: 

```
tccli billing DescribeBillSummaryByRegion --cli-unfold-argument  \
    --PayerUin 909619400 \
    --BeginTime '2018-11-01 00:00:00' \
    --EndTime '2018-11-01 23:59:59'
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryOverview": [
            {
                "RegionId": "4",
                “RealTotalCost": "1330.52",
                "CashPayAmount": "1330.52",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "83.26",
                "BillMonth": "2018-11",
                "RegionName": "East China (Shanghai)",
            },
            {
                "RegionId": "1",
                “RealTotalCost": "200.85",
                "CashPayAmount": "24.87",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "175.99",
                "RealTotalCostRatio": "12.57",
                "BillMonth": "2018-11",
                "RegionName": "South China (Guangzhou)"
            },
            {
                "RegionId": "8",
                “RealTotalCost": "66.58",
                "CashPayAmount": "66.58",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "4.17",
                "BillMonth": "2018-11",
                "RegionName": "North China (Beijing)",
            },
            {
                "RegionId": "16",
                “RealTotalCost": "0.02",
                "CashPayAmount": "0.02",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Southwest China (Chengdu)"
            },
            {
                "RegionId": "19",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Southwest China (Chongqing)"
            },
            {
                "RegionId": "24",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Europe (Moscow)"
            },
            {
                "RegionId": "6",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "North America (Toronto)",
            },
            {
                "RegionId": "9",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Southeast Asia (Singapore)",
            },
            {
                "RegionId": "17",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Europe (Germany)"
            },
            {
                "RegionId": "5",
                “RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Hong Kong/Macao/Taiwan, China region (Hong Kong, China)"
            },
            {
                "RegionId": "0",
                “RealTotalCost": "-1.49",
                "CashPayAmount": "-1.50",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.01",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "Others",
            }
        ],
        "RequestId": "88268803-850d-44bc-8d64-df857c2d7487"
    }
}
```

