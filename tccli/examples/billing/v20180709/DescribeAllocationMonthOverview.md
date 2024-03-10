**Example 1: 查询分账报表月概览**



Input: 

```
tccli billing DescribeAllocationMonthOverview --cli-unfold-argument  \
    --Month 2022-11-01 00:00:00
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "Id": 616417,
                "Name": "集团",
                "TreeNodeUniqKey": "xxxx-63871c5ede811",
                "Symbol": 0,
                "Children": [
                    {
                        "Id": 835454,
                        "Name": "财务产品",
                        "TreeNodeUniqKey": "xxxx-6391da70528fb",
                        "Symbol": 0,
                        "Children": [
                            {
                                "Id": 835457,
                                "Name": "核算组",
                                "TreeNodeUniqKey": "xxxx-6391da9ae376c",
                                "Symbol": 1,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "0.00000000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "0.00000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.00000000",
                                    "GatherCashPayAmount": "0.00000000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "0.00000000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "0.00000000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.00",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            },
                            {
                                "Id": 835458,
                                "Name": "核算组（新）",
                                "TreeNodeUniqKey": "xxxx-6391dab1d770f",
                                "Symbol": 2,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "0.00000000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "0.00000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.00000000",
                                    "GatherCashPayAmount": "38.31000000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "38.31000000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "38.31000000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.10",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            },
                            {
                                "Id": 835459,
                                "Name": "资金组",
                                "TreeNodeUniqKey": "xxxx-6391dabf3a789",
                                "Symbol": 1,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "153.09000000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "154.70000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "1.61000000",
                                    "GatherCashPayAmount": "191.03800000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "191.03800000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "345.73800000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.94",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            },
                            {
                                "Id": 835460,
                                "Name": "结算组",
                                "TreeNodeUniqKey": "xxxx-6391dac6c4f72",
                                "Symbol": 1,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "33.30600000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "33.57000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.26400000",
                                    "GatherCashPayAmount": "71.34000000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "71.34000000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "104.91000000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.28",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            }
                        ],
                        "Detail": {
                            "AllocateCashPayAmount": "186.39600000",
                            "AllocateIncentivePayAmount": "0.00000000",
                            "AllocateRealCost": "188.27000000",
                            "AllocateTransferPayAmount": "0.00000000",
                            "AllocateVoucherPayAmount": "1.87400000",
                            "GatherCashPayAmount": "300.68800000",
                            "GatherIncentivePayAmount": "0.00000000",
                            "GatherRealCost": "300.68800000",
                            "GatherTransferPayAmount": "0.00000000",
                            "GatherVoucherPayAmount": "0.00000000",
                            "RealTotalCost": "488.95800000",
                            "TotalCashPayAmount": "0.00000000",
                            "TotalIncentivePayAmount": "0.00000000",
                            "TotalTransferPayAmount": "0.00000000",
                            "TotalVoucherPayAmount": "0.00000000",
                            "Ratio": "1.32",
                            "Trend": null,
                            "TrendType": "none"
                        }
                    },
                    {
                        "Id": 835455,
                        "Name": "营销产品",
                        "TreeNodeUniqKey": "xxxx-6391da78a09a4",
                        "Symbol": 0,
                        "Children": [
                            {
                                "Id": 835461,
                                "Name": "主数据组",
                                "TreeNodeUniqKey": "xxxx-6391dad853206",
                                "Symbol": 2,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "0.00000000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "0.00000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.00000000",
                                    "GatherCashPayAmount": "295.95000000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "298.67000000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "2.72000000",
                                    "RealTotalCost": "298.67000000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.81",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            },
                            {
                                "Id": 835462,
                                "Name": "客户应用组",
                                "TreeNodeUniqKey": "xxxx-6391dae9802da",
                                "Symbol": 1,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "1047.14500000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "1047.14500000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.00000000",
                                    "GatherCashPayAmount": "54.32717665",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "54.37717665",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.05000000",
                                    "RealTotalCost": "1101.52217665",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "2.98",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            }
                        ],
                        "Detail": {
                            "AllocateCashPayAmount": "1047.14500000",
                            "AllocateIncentivePayAmount": "0.00000000",
                            "AllocateRealCost": "1047.14500000",
                            "AllocateTransferPayAmount": "0.00000000",
                            "AllocateVoucherPayAmount": "0.00000000",
                            "GatherCashPayAmount": "350.27717665",
                            "GatherIncentivePayAmount": "0.00000000",
                            "GatherRealCost": "353.04717665",
                            "GatherTransferPayAmount": "0.00000000",
                            "GatherVoucherPayAmount": "2.77000000",
                            "RealTotalCost": "1400.19217665",
                            "TotalCashPayAmount": "0.00000000",
                            "TotalIncentivePayAmount": "0.00000000",
                            "TotalTransferPayAmount": "0.00000000",
                            "TotalVoucherPayAmount": "0.00000000",
                            "Ratio": "3.79",
                            "Trend": null,
                            "TrendType": "none"
                        }
                    },
                    {
                        "Id": 835456,
                        "Name": "数据产品",
                        "TreeNodeUniqKey": "xxxx-6391da8abb3c7",
                        "Symbol": 0,
                        "Children": [
                            {
                                "Id": 835467,
                                "Name": "数据产品-自动创建",
                                "TreeNodeUniqKey": "xxxx-63929e07089d0",
                                "Symbol": 1,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "1124.85900000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "1125.47500000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.61600000",
                                    "GatherCashPayAmount": "13.31482335",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "13.31482335",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "1138.78982335",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "3.08",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            },
                            {
                                "Id": 835468,
                                "Name": "1",
                                "TreeNodeUniqKey": "xxxx-63929e0706e81",
                                "Symbol": 0,
                                "Children": null,
                                "Detail": {
                                    "AllocateCashPayAmount": "0.00000000",
                                    "AllocateIncentivePayAmount": "0.00000000",
                                    "AllocateRealCost": "0.00000000",
                                    "AllocateTransferPayAmount": "0.00000000",
                                    "AllocateVoucherPayAmount": "0.00000000",
                                    "GatherCashPayAmount": "0.00000000",
                                    "GatherIncentivePayAmount": "0.00000000",
                                    "GatherRealCost": "0.00000000",
                                    "GatherTransferPayAmount": "0.00000000",
                                    "GatherVoucherPayAmount": "0.00000000",
                                    "RealTotalCost": "0.00000000",
                                    "TotalCashPayAmount": "0.00000000",
                                    "TotalIncentivePayAmount": "0.00000000",
                                    "TotalTransferPayAmount": "0.00000000",
                                    "TotalVoucherPayAmount": "0.00000000",
                                    "Ratio": "0.00",
                                    "Trend": null,
                                    "TrendType": "none"
                                }
                            }
                        ],
                        "Detail": {
                            "AllocateCashPayAmount": "1124.85900000",
                            "AllocateIncentivePayAmount": "0.00000000",
                            "AllocateRealCost": "1125.47500000",
                            "AllocateTransferPayAmount": "0.00000000",
                            "AllocateVoucherPayAmount": "0.61600000",
                            "GatherCashPayAmount": "13.31482335",
                            "GatherIncentivePayAmount": "0.00000000",
                            "GatherRealCost": "13.31482335",
                            "GatherTransferPayAmount": "0.00000000",
                            "GatherVoucherPayAmount": "0.00000000",
                            "RealTotalCost": "1138.78982335",
                            "TotalCashPayAmount": "0.00000000",
                            "TotalIncentivePayAmount": "0.00000000",
                            "TotalTransferPayAmount": "0.00000000",
                            "TotalVoucherPayAmount": "0.00000000",
                            "Ratio": "3.08",
                            "Trend": null,
                            "TrendType": "none"
                        }
                    }
                ],
                "Detail": {
                    "AllocateCashPayAmount": "2358.40000000",
                    "AllocateIncentivePayAmount": "0.00000000",
                    "AllocateRealCost": "2360.89000000",
                    "AllocateTransferPayAmount": "0.00000000",
                    "AllocateVoucherPayAmount": "2.49000000",
                    "GatherCashPayAmount": "664.28000000",
                    "GatherIncentivePayAmount": "0.00000000",
                    "GatherRealCost": "667.05000000",
                    "GatherTransferPayAmount": "0.00000000",
                    "GatherVoucherPayAmount": "2.77000000",
                    "RealTotalCost": "3027.94000000",
                    "TotalCashPayAmount": "0.00000000",
                    "TotalIncentivePayAmount": "0.00000000",
                    "TotalTransferPayAmount": "0.00000000",
                    "TotalVoucherPayAmount": "0.00000000",
                    "Ratio": "8.20",
                    "Trend": "0.00",
                    "TrendType": "upward"
                }
            },
            {
                "Id": null,
                "Name": "未分配",
                "TreeNodeUniqKey": "",
                "Symbol": 0,
                "Children": null,
                "Detail": {
                    "AllocateCashPayAmount": "0.00000000",
                    "AllocateIncentivePayAmount": "0.00000000",
                    "AllocateRealCost": "0.00000000",
                    "AllocateTransferPayAmount": "0.00000000",
                    "AllocateVoucherPayAmount": "0.00000000",
                    "GatherCashPayAmount": "33882.13000000",
                    "GatherIncentivePayAmount": "0.00000000",
                    "GatherRealCost": "33888.87000000",
                    "GatherTransferPayAmount": "0.00000000",
                    "GatherVoucherPayAmount": "6.74000000",
                    "RealTotalCost": "33888.87000000",
                    "TotalCashPayAmount": "0.00000000",
                    "TotalIncentivePayAmount": "0.00000000",
                    "TotalTransferPayAmount": "0.00000000",
                    "TotalVoucherPayAmount": "0.00000000",
                    "Ratio": "91.80",
                    "Trend": "5096.05",
                    "TrendType": "upward"
                }
            }
        ],
        "Total": {
            "RealTotalCost": "36916.81000000",
            "CashPayAmount": "36904.81000000",
            "IncentivePayAmount": "0.00000000",
            "VoucherPayAmount": "12.00000000",
            "TransferPayAmount": "0.00000000"
        },
        "RequestId": "xxxx"
    }
}
```

