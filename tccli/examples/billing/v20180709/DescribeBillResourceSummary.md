**Example 1: 获取账单资源汇总**

获取账单资源汇总

Input: 

```
tccli billing DescribeBillResourceSummary --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --PeriodType byPayTime \
    --Month 2022-01 \
    --NeedRecordNum 1
```

Output: 
```
{
    "Response": {
        "ResourceSummarySet": [
            {
                "BusinessCodeName": "内容分发网络 CDN",
                "ProductCodeName": "中国境外CDN",
                "PayModeName": "按量计费",
                "ProjectName": "默认项目",
                "RegionName": "亚太地区（亚太一区）",
                "ZoneName": "其他",
                "ResourceId": "125391_sv_cdn_ux_AS1_1",
                "ResourceName": "rName",
                "ActionTypeName": "按量计费小时结",
                "OrderId": "6074d5d00 ",
                "PayTime": "2020-09-22 00:00:00",
                "FeeBeginTime": "2020-09-22 00:00:00",
                "FeeEndTime": "2020-09-22 00:00:00",
                "ConfigDesc": "config desc",
                "ExtendField1": "6074d5d00 ",
                "ExtendField2": "6074d5d00",
                "TotalCost": "4.84660512",
                "Discount": "1",
                "ReduceType": "折扣",
                "RealTotalCost": "4.84660512",
                "VoucherPayAmount": "0.00000000",
                "CashPayAmount": "4.84660512",
                "IncentivePayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "ExtendField3": "extend file ",
                "ExtendField4": "extend file",
                "ExtendField5": "extend file",
                "Tags": [
                    {
                        "TagKey": "tk_1",
                        "TagValue": "tv_1"
                    }
                ],
                "PayerUin": "909619400",
                "OwnerUin": "909619400",
                "OperateUin": "909619400",
                "BusinessCode": "p_cdn",
                "ProductCode": "sp_cdn_ov",
                "RegionId": 1001,
                "InstanceType": "it",
                "OriginalCostWithRI": "0.00000000",
                "SPDeduction": "0.00000000",
                "OriginalCostWithSP": "0.00000000"
            }
        ],
        "Total": 0,
        "RequestId": "6074d5d00-6074d5d00 "
    }
}
```

