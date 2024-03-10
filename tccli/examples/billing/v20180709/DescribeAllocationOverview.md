**Example 1: DescribeAllocationOverview**



Input: 

```
tccli billing DescribeAllocationOverview --cli-unfold-argument  \
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
                "TreeNodeUniqKey": "700000384179-6376f0b3ada52",
                "GatherCashPayAmount": "8072.80000000",
                "GatherVoucherPayAmount": "0.00000000",
                "GatherIncentivePayAmount": "0.00000000",
                "GatherTransferPayAmount": "0.00000000",
                "AllocateCashPayAmount": "0.00000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "TotalCashPayAmount": "0.00000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "0.00000000",
                "GatherRealCost": "8072.80000000",
                "AllocateRealCost": "0.00000000",
                "RealTotalCost": "8072.80000000",
                "TreeNodeUniqKeyName": "HR产品",
                "Ratio": "99.65",
                "Trend": null,
                "TrendType": "none",
                "BillDate": null
            },
            {
                "TreeNodeUniqKey": "700000384179-63733abacc8b8",
                "GatherCashPayAmount": "0.00000000",
                "GatherVoucherPayAmount": "0.00000000",
                "GatherIncentivePayAmount": "0.00000000",
                "GatherTransferPayAmount": "0.00000000",
                "AllocateCashPayAmount": "14.16000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "TotalCashPayAmount": "0.00000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "0.00000000",
                "GatherRealCost": "0.00000000",
                "AllocateRealCost": "14.16000000",
                "RealTotalCost": "14.16000000",
                "TreeNodeUniqKeyName": "计费临时项目",
                "Ratio": "0.17",
                "Trend": null,
                "TrendType": "none",
                "BillDate": null
            },
            {
                "TreeNodeUniqKey": "700000384179-63733ac7e46ff",
                "GatherCashPayAmount": "0.00000000",
                "GatherVoucherPayAmount": "0.00000000",
                "GatherIncentivePayAmount": "0.00000000",
                "GatherTransferPayAmount": "0.00000000",
                "AllocateCashPayAmount": "14.16000000",
                "AllocateVoucherPayAmount": "0.00000000",
                "AllocateIncentivePayAmount": "0.00000000",
                "AllocateTransferPayAmount": "0.00000000",
                "TotalCashPayAmount": "0.00000000",
                "TotalVoucherPayAmount": "0.00000000",
                "TotalIncentivePayAmount": "0.00000000",
                "TotalTransferPayAmount": "0.00000000",
                "GatherRealCost": "0.00000000",
                "AllocateRealCost": "14.16000000",
                "RealTotalCost": "14.16000000",
                "TreeNodeUniqKeyName": "中期调整项目",
                "Ratio": "0.17",
                "Trend": null,
                "TrendType": "none",
                "BillDate": null
            }
        ],
        "RecordNum": 3,
        "Total": {
            "RealTotalCost": "8101.12000000",
            "CashPayAmount": "8101.12000000",
            "IncentivePayAmount": "0.00000000",
            "VoucherPayAmount": "0.00000000",
            "TransferPayAmount": "0.00000000"
        },
        "RequestId": "db3c4d66-ce51-4b94-91d0-c65c7938475b"
    }
}
```

