**Example 1: 查询分账账单按资源汇总**



Input: 

```
tccli billing DescribeAllocationSummaryByResource --cli-unfold-argument  \
    --Month 2022-11-01 00:00:00 \
    --Limit 30 \
    --Offset 0 \
    --PeriodType month
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "ActionType": "postpay_deduct_d",
                "ActionTypeName": "按量计费日结",
                "AllocationType": 1,
                "BillDate": "2024-02-01",
                "BusinessCode": "p_cos",
                "BusinessCodeName": "COS 对象存储",
                "CashPayAmount": "0.00001027",
                "ComponentConfig": "COS 标准存储存储容量: 0.00390625 GB",
                "FeeBeginTime": "2024-02-01 00:00:00",
                "FeeEndTime": "2024-02-01 23:59:59",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": null,
                "InstanceTypeName": "-",
                "OperateUin": "909619400",
                "OwnerUin": "909619400",
                "PayMode": "postPay",
                "PayModeName": "按量计费",
                "PayerUin": "909619400",
                "ProductCode": "sp_cos_std",
                "ProductCodeName": "COS 标准存储",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "RealTotalCost": "0.00001027",
                "RegionId": 33,
                "RegionName": "华东地区（南京）",
                "RegionType": "domestic",
                "RegionTypeName": "国内",
                "ResourceId": "909619400-std_storage-19",
                "ResourceName": null,
                "RiCost": "0.00000000",
                "RiTimeSpan": "0.00000000",
                "SPCost": "0.00000000",
                "SplitItemId": "1234567-1251007194",
                "SplitItemName": "1234567",
                "Tag": [
                    {
                        "TagKey": "游戏项目组",
                        "TagValue": "火影忍者"
                    }
                ],
                "TotalCost": "0.00001537",
                "TransferPayAmount": "0.00000000",
                "TreeNodeUniqKey": "909619400-659bb8eb2830e",
                "TreeNodeUniqKeyName": "研究组",
                "VoucherPayAmount": "0.00000000",
                "ZoneId": 330001,
                "ZoneName": "南京一区"
            }
        ],
        "RecordNum": 30592,
        "RequestId": "4b163951-0990-442b-922c-cf5145fd1e56",
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

