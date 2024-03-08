**Example 1: 查询分账账单按产品汇总**



Input: 

```
tccli billing DescribeAllocationSummaryByBusiness --cli-unfold-argument  \
    --Limit 30 \
    --Month 2022-11-01 00:00:00 \
    --Offset 0 \
    --PeriodType month
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "AllocateCashPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateRealCost": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocationRealTotalCost": "-48.95000000",
                "BillDate": "2024-02-01",
                "BusinessCode": "p_ci",
                "BusinessCodeName": "数据万象CI",
                "CashPayAmount": "-16.43000000",
                "GatherCashPayAmount": "-16.43000000",
                "GatherIncentivePayAmount": "-32.52000000",
                "GatherRealCost": "-48.95000000",
                "GatherTransferPayAmount": "0.00000000",
                "GatherVoucherPayAmount": "0.00000000",
                "IncentivePayAmount": "0.00000000",
                "RICost": "0.00000000",
                "Ratio": "-0.15",
                "RealTotalCost": "-48.95000000",
                "SPCost": "0.00000000",
                "TotalCashPayAmount": "-16.43000000",
                "TotalCost": "-48.95000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "-32.52000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TransferPayAmount": "-32.52000000",
                "TreeNodeUniqKey": null,
                "TreeNodeUniqKeyName": "未分配",
                "Trend": null,
                "TrendType": null,
                "VoucherPayAmount": "0.00000000"
            },
            {
                "AllocateCashPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateRealCost": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocationRealTotalCost": "-2365.08000000",
                "BillDate": "2024-02-01",
                "BusinessCode": "p_rav",
                "BusinessCodeName": "实时音视频",
                "CashPayAmount": "0.00000000",
                "GatherCashPayAmount": "0.00000000",
                "GatherIncentivePayAmount": "-2365.08000000",
                "GatherRealCost": "-2365.08000000",
                "GatherTransferPayAmount": "0.00000000",
                "GatherVoucherPayAmount": "0.00000000",
                "IncentivePayAmount": "0.00000000",
                "RICost": "0.00000000",
                "Ratio": "-7.18",
                "RealTotalCost": "-2365.08000000",
                "SPCost": "0.00000000",
                "TotalCashPayAmount": "0.00000000",
                "TotalCost": "-2365.08000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "-2365.08000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TransferPayAmount": "-2365.08000000",
                "TreeNodeUniqKey": null,
                "TreeNodeUniqKeyName": "未分配",
                "Trend": null,
                "TrendType": null,
                "VoucherPayAmount": "0.00000000"
            },
            {
                "AllocateCashPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateRealCost": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocationRealTotalCost": "0.00000000",
                "BillDate": "2024-02-01",
                "BusinessCode": "p_ccc",
                "BusinessCodeName": "云联络中心",
                "CashPayAmount": "0.00000000",
                "GatherCashPayAmount": "0.00000000",
                "GatherIncentivePayAmount": "0.00000000",
                "GatherRealCost": "0.00000000",
                "GatherTransferPayAmount": "0.00000000",
                "GatherVoucherPayAmount": "0.00000000",
                "IncentivePayAmount": "0.00000000",
                "RICost": "0.00000000",
                "Ratio": "0.00",
                "RealTotalCost": "0.00000000",
                "SPCost": "0.00000000",
                "TotalCashPayAmount": "0.00000000",
                "TotalCost": "263.44000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "0.00000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": null,
                "TreeNodeUniqKeyName": "未分配",
                "Trend": null,
                "TrendType": null,
                "VoucherPayAmount": "0.00000000"
            }
        ],
        "RecordNum": 611,
        "RequestId": "1cd9694c-88a7-4cfe-846c-182f1f9dbf6c",
        "Total": {
            "CashPayAmount": "1630.93000000",
            "IncentivePayAmount": "31062.86000000",
            "RealTotalCost": "32953.81000000",
            "TransferPayAmount": "0.00000000",
            "VoucherPayAmount": "260.02000000"
        }
    }
}
```

