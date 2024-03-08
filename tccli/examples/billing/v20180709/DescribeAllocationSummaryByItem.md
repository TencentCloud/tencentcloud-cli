**Example 1: 查询分账账单按组件汇总**

查询分账账单按组件汇总

Input: 

```
tccli billing DescribeAllocationSummaryByItem --cli-unfold-argument  \
    --Month 2024-02 \
    --Limit 1 \
    --Offset 0 \
    --PeriodType month
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "ActionType": "billVirtualId",
                "ActionTypeName": "月度计费精度差异",
                "AllocationType": 1,
                "BillDate": null,
                "BlendedDiscount": "-",
                "BusinessCode": "billVirtualId",
                "BusinessCodeName": "月度计费精度差异",
                "CashPayAmount": "-0.00000285",
                "ComponentCode": "billVirtualId",
                "ComponentCodeName": "月度计费精度差异",
                "ComponentConfig": "",
                "ContractPrice": "-0.00000285",
                "DeductedMeasure": "-",
                "Discount": "-",
                "FeeBeginTime": "2024-02-01 00:00:00",
                "FeeEndTime": "2024-02-07 23:59:59",
                "Formula": "-",
                "FormulaUrl": "",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": null,
                "InstanceTypeName": "-",
                "ItemCode": "billVirtualId",
                "ItemCodeName": "月度计费精度差异",
                "OperateUin": "909619400",
                "OwnerUin": "909619400",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "PayerUin": "909619400",
                "PriceInfo": [],
                "ProductCode": "billVirtualId",
                "ProductCodeName": "月度计费精度差异",
                "ProjectId": 0,
                "ProjectName": "扣费精度补偿",
                "RealTotalCost": "-0.00000285",
                "RealTotalMeasure": "-",
                "RegionId": 0,
                "RegionName": "其他",
                "RegionType": "other",
                "RegionTypeName": "其他",
                "ReserveDetail": "",
                "ResourceId": "909619400(UIN)",
                "ResourceName": "扣费精度补偿",
                "RiCost": "0.00000000",
                "RiTimeSpan": "0.00000000",
                "SPCost": "0.00000000",
                "SinglePrice": "-0.00000285",
                "SinglePriceUnit": "元/月",
                "SplitItemId": "-",
                "SplitItemName": "-",
                "Tag": null,
                "TimeSpan": "1.00000000",
                "TimeUnit": "月",
                "TotalCost": "-0.00000285",
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": "909619400-6391dae9802da",
                "TreeNodeUniqKeyName": "客户应用组",
                "UsedAmount": "1.00000000",
                "UsedAmountUnit": "",
                "VoucherPayAmount": "0.00000000",
                "ZoneId": 0,
                "ZoneName": "其他"
            }
        ],
        "RecordNum": 18411,
        "RequestId": "ceb74979-c668-42f6-b266-57541de2f755",
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

