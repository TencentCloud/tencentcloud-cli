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
                "BusinessCodeName": "abc",
                "ProductCodeName": "abc",
                "PayModeName": "abc",
                "ProjectName": "abc",
                "RegionName": "abc",
                "ZoneName": "abc",
                "ResourceId": "abc",
                "ResourceName": "abc",
                "ActionTypeName": "abc",
                "OrderId": "abc",
                "PayTime": "2020-09-22 00:00:00",
                "FeeBeginTime": "2020-09-22 00:00:00",
                "FeeEndTime": "2020-09-22 00:00:00",
                "ConfigDesc": "abc",
                "ExtendField1": "abc",
                "ExtendField2": "abc",
                "TotalCost": "abc",
                "Discount": "abc",
                "ReduceType": "abc",
                "RealTotalCost": "abc",
                "VoucherPayAmount": "abc",
                "CashPayAmount": "abc",
                "IncentivePayAmount": "abc",
                "TransferPayAmount": "abc",
                "ExtendField3": "abc",
                "ExtendField4": "abc",
                "ExtendField5": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "PayerUin": "abc",
                "OwnerUin": "abc",
                "OperateUin": "abc",
                "BusinessCode": "abc",
                "ProductCode": "abc",
                "RegionId": 0,
                "InstanceType": "abc",
                "OriginalCostWithRI": "abc",
                "SPDeduction": "abc",
                "OriginalCostWithSP": "abc"
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

