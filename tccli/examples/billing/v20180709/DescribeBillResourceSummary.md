**Example 1: 获取账单资源汇总**



Input: 

```
tccli billing DescribeBillResourceSummary --cli-unfold-argument  \
    --Month 2018-08 \
    --PeriodType byPayTime \
    --Offset 0 \
    --Limit 1 \
    --ActionType 按量计费扣费
```

Output: 
```
{
    "Response": {
        "Total": 103,
        "RequestId": "xx",
        "ResourceSummarySet": [
            {
                "ReduceType": "xx",
                "SPDeduction": "xx",
                "ProductCode": "xx",
                "FeeEndTime": "2020-09-22 00:00:00",
                "CashPayAmount": "xx",
                "ProductCodeName": "xx",
                "ActionTypeName": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ResourceId": "xx",
                "RegionId": 0,
                "ConfigDesc": "xx",
                "Discount": "xx",
                "ResourceName": "xx",
                "InstanceType": "xx",
                "RegionName": "xx",
                "TotalCost": "xx",
                "BusinessCode": "xx",
                "RealTotalCost": "xx",
                "OwnerUin": "xx",
                "PayerUin": "xx",
                "ExtendField4": "xx",
                "OperateUin": "xx",
                "BusinessCodeName": "xx",
                "OrderId": "xx",
                "ExtendField1": "xx",
                "ExtendField2": "xx",
                "ExtendField3": "xx",
                "VoucherPayAmount": "xx",
                "ExtendField5": "xx",
                "PayModeName": "xx",
                "OriginalCostWithRI": "xx",
                "FeeBeginTime": "2020-09-22 00:00:00",
                "IncentivePayAmount": "xx",
                "ProjectName": "xx",
                "PayTime": "2020-09-22 00:00:00",
                "OriginalCostWithSP": "xx",
                "ZoneName": "xx"
            }
        ]
    }
}
```

