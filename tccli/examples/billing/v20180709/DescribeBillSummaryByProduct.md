**Example 1: 获取产品汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByProduct --cli-unfold-argument  \
    --BeginTime 2018-11 \
    --EndTime 2018-11
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryTotal": {
            "RealTotalCost": "224.81",
            "TotalCost": "-",
            "VoucherPayAmount": "18.69",
            "IncentivePayAmount": "0.00",
            "CashPayAmount": "206.12"
        },
        "SummaryOverview": [
            {
                "BusinessCode": "p_cdn",
                "RealTotalCost": "113.02",
                "TotalCost": "-",
                "CashPayAmount": "113.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.02",
                "RealTotalCostRatio": "50.27",
                "BillMonth": "2021-01",
                "BusinessCodeName": "内容分发网络 CDN"
            },
            {
                "BusinessCode": "p_cos",
                "RealTotalCost": "54.22",
                "TotalCost": "-",
                "CashPayAmount": "54.22",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "24.12",
                "BillMonth": "2021-01",
                "BusinessCodeName": "COS 对象存储"
            },
            {
                "BusinessCode": "p_cvm",
                "RealTotalCost": "37.71",
                "TotalCost": "-",
                "CashPayAmount": "21.32",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "16.39",
                "RealTotalCostRatio": "16.78",
                "BillMonth": "2021-01",
                "BusinessCodeName": "云服务器CVM"
            },
            {
                "BusinessCode": "p_cdb",
                "RealTotalCost": "16.88",
                "TotalCost": "-",
                "CashPayAmount": "16.88",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "7.51",
                "BillMonth": "2021-01",
                "BusinessCodeName": "云数据库MySQL"
            },
            {
                "BusinessCode": "billVirtualId",
                "RealTotalCost": "2.98",
                "TotalCost": "-",
                "CashPayAmount": "0.70",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "2.28",
                "RealTotalCostRatio": "1.32",
                "BillMonth": "2021-01",
                "BusinessCodeName": "月度计费精度差异"
            },
            {
                "BusinessCode": "p_market",
                "RealTotalCost": "0.00",
                "TotalCost": "-",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2021-01",
                "BusinessCodeName": "云市场"
            }
        ],
        "RequestId": "bae960ff-ee67-49c8-b4a6-d93475e2e696"
    }
}
```

