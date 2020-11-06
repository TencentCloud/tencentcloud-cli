**Example 1: 获取按地域汇总费用分布**



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
                "RealTotalCost": "1330.52",
                "CashPayAmount": "1330.52",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "83.26",
                "BillMonth": "2018-11",
                "RegionName": "华东地区（上海）"
            },
            {
                "RegionId": "1",
                "RealTotalCost": "200.85",
                "CashPayAmount": "24.87",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "175.99",
                "RealTotalCostRatio": "12.57",
                "BillMonth": "2018-11",
                "RegionName": "华南地区（广州）"
            },
            {
                "RegionId": "8",
                "RealTotalCost": "66.58",
                "CashPayAmount": "66.58",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "4.17",
                "BillMonth": "2018-11",
                "RegionName": "华北地区（北京）"
            },
            {
                "RegionId": "16",
                "RealTotalCost": "0.02",
                "CashPayAmount": "0.02",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "西南地区（成都）"
            },
            {
                "RegionId": "19",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "西南地区（重庆）"
            },
            {
                "RegionId": "24",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "欧洲地区（莫斯科）"
            },
            {
                "RegionId": "6",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "北美地区（多伦多）"
            },
            {
                "RegionId": "9",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "东南亚地区（新加坡）"
            },
            {
                "RegionId": "17",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "欧洲地区（德国）"
            },
            {
                "RegionId": "5",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "港澳台地区（中国香港）"
            },
            {
                "RegionId": "0",
                "RealTotalCost": "-1.49",
                "CashPayAmount": "-1.50",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.01",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "RegionName": "其他"
            }
        ],
        "RequestId": "88268803-850d-44bc-8d64-df857c2d7487"
    }
}
```

