**Example 1: 查询分账明细**

查询分账明细

Input: 

```
tccli billing DescribeAllocationBillDetail --cli-unfold-argument  \
    --Month 2023-02-01 00:00:00 \
    --Limit 2 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "ActionType": "postpay_deduct_h",
                "ActionTypeName": "按量计费小时结",
                "BillDate": "2023-02-05",
                "BillId": "20230205400491987853552",
                "BlendedDiscount": "0.33548100",
                "BusinessCode": "p_eks",
                "BusinessCodeName": "Serverless 容器服务",
                "CashPayAmount": "0.01677073",
                "ComponentCode": "v_eks_mem",
                "ComponentCodeName": "内存",
                "ContractPrice": "0.00000466",
                "Discount": "0.33548100",
                "FeeBeginTime": "2023-02-05 10:00:00",
                "FeeEndTime": "2023-02-05 10:59:59",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": null,
                "InstanceTypeName": "-",
                "ItemCode": "sv_eks_mem",
                "ItemCodeName": "弹性容器服务EKS-内存",
                "OperateUin": "909619400",
                "OrderId": "-",
                "OwnerUin": "909619400",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "PayTime": "2023-02-05 11:46:29",
                "PayerUin": "909619400",
                "ProductCode": "sp_eks_standard_pod",
                "ProductCodeName": "弹性容器服务EKS-Pod",
                "ProjectId": 0,
                "ProjectName": null,
                "RICost": "0.00000000",
                "RITimeSpan": "0.00000000",
                "RealTotalCost": "0.01677073",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "RegionType": "domestic",
                "RegionTypeName": "国内",
                "ReserveDetail": "",
                "ResourceId": "eks-bzmzprry",
                "ResourceName": null,
                "SPCost": "0.00000000",
                "SinglePrice": "0.00001389",
                "SinglePriceUnit": "元/GiB/秒",
                "SplitRatio": "0.00000000",
                "Tag": null,
                "TimeSpan": "3599.00000000",
                "TimeUnit": "秒",
                "TotalCost": "0.04999011",
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": null,
                "TreeNodeUniqKeyName": "未分配",
                "UsedAmount": "1.00000000",
                "UsedAmountUnit": "GiB",
                "VoucherPayAmount": "0.00000000",
                "ZoneId": 100004,
                "ZoneName": "广州四区"
            },
            {
                "ActionType": "postpay_deduct_h",
                "ActionTypeName": "按量计费小时结",
                "BillDate": "2023-02-05",
                "BillId": "20230205400491961266162",
                "BlendedDiscount": "0.33548100",
                "BusinessCode": "p_eks",
                "BusinessCodeName": "Serverless 容器服务",
                "CashPayAmount": "0.01677073",
                "ComponentCode": "v_eks_mem",
                "ComponentCodeName": "内存",
                "ContractPrice": "0.00000466",
                "Discount": "0.33548100",
                "FeeBeginTime": "2023-02-05 09:00:00",
                "FeeEndTime": "2023-02-05 09:59:59",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": null,
                "InstanceTypeName": "-",
                "ItemCode": "sv_eks_mem",
                "ItemCodeName": "弹性容器服务EKS-内存",
                "OperateUin": "909619400",
                "OrderId": "-",
                "OwnerUin": "909619400",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "PayTime": "2023-02-05 11:09:31",
                "PayerUin": "909619400",
                "ProductCode": "sp_eks_standard_pod",
                "ProductCodeName": "弹性容器服务EKS-Pod",
                "ProjectId": 0,
                "ProjectName": null,
                "RICost": "0.00000000",
                "RITimeSpan": "0.00000000",
                "RealTotalCost": "0.01677073",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "RegionType": "domestic",
                "RegionTypeName": "国内",
                "ReserveDetail": "",
                "ResourceId": "eks-bzmzprry",
                "ResourceName": null,
                "SPCost": "0.00000000",
                "SinglePrice": "0.00001389",
                "SinglePriceUnit": "元/GiB/秒",
                "SplitRatio": "0.00000000",
                "Tag": null,
                "TimeSpan": "3599.00000000",
                "TimeUnit": "秒",
                "TotalCost": "0.04999011",
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": null,
                "TreeNodeUniqKeyName": "未分配",
                "UsedAmount": "1.00000000",
                "UsedAmountUnit": "GiB",
                "VoucherPayAmount": "0.00000000",
                "ZoneId": 100004,
                "ZoneName": "广州四区"
            }
        ],
        "RecordNum": 33751,
        "RequestId": "48d52cbc-2297-4ba5-a322-de477fed6329",
        "Total": {
            "CashPayAmount": "99034.51148297",
            "IncentivePayAmount": "0.00000000",
            "RealTotalCost": "99067.91144815",
            "TransferPayAmount": "0.00000000",
            "VoucherPayAmount": "130.94995680"
        }
    }
}
```

