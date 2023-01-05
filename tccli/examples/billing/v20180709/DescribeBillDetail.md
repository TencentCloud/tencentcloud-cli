**Example 1: 获取账单明细**



Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --ResourceId ins-49zhx6z1 \
    --NeedRecordNum 1 \
    --PeriodType byPayTime \
    --Month 2018-07 \
    --Limit 1 \
    --BeginTime 2018-11-0100:00:00 \
    --Offset 0 \
    --EndTime 2018-11-0123:59:59
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "DetailSet": [
            {
                "BusinessCode": "xx",
                "ComponentSet": [
                    {
                        "ReduceType": "xx",
                        "BlendedDiscount": "xx",
                        "RealCost": "xx",
                        "SPDeduction": "xx",
                        "TimeSpan": "xx",
                        "CashPayAmount": "xx",
                        "SpecifiedPrice": "xx",
                        "Discount": "xx",
                        "OriginalCostWithRI": "xx",
                        "InstanceType": "xx",
                        "TimeUnitName": "xx",
                        "ComponentCode": "xx",
                        "SinglePrice": "xx",
                        "ContractPrice": "xx",
                        "UsedAmountUnit": "xx",
                        "ItemCodeName": "xx",
                        "VoucherPayAmount": "xx",
                        "RiTimeSpan": "xx",
                        "SPDeductionRate": "xx",
                        "PriceUnit": "xx",
                        "ComponentCodeName": "xx",
                        "ItemCode": "xx",
                        "Cost": "xx",
                        "IncentivePayAmount": "xx",
                        "UsedAmount": "xx",
                        "OriginalCostWithSP": "xx"
                    },
                    {
                        "ReduceType": "xx",
                        "BlendedDiscount": "xx",
                        "RealCost": "xx",
                        "SPDeduction": "xx",
                        "TimeSpan": "xx",
                        "CashPayAmount": "xx",
                        "SpecifiedPrice": "xx",
                        "Discount": "xx",
                        "OriginalCostWithRI": "xx",
                        "InstanceType": "xx",
                        "TimeUnitName": "xx",
                        "ComponentCode": "xx",
                        "SinglePrice": "xx",
                        "ContractPrice": "xx",
                        "UsedAmountUnit": "xx",
                        "ItemCodeName": "xx",
                        "VoucherPayAmount": "xx",
                        "RiTimeSpan": "xx",
                        "SPDeductionRate": "xx",
                        "PriceUnit": "xx",
                        "ComponentCodeName": "xx",
                        "ItemCode": "xx",
                        "Cost": "xx",
                        "IncentivePayAmount": "xx",
                        "UsedAmount": "xx",
                        "OriginalCostWithSP": "xx"
                    },
                    {
                        "ReduceType": "xx",
                        "BlendedDiscount": "xx",
                        "RealCost": "xx",
                        "SPDeduction": "xx",
                        "TimeSpan": "xx",
                        "CashPayAmount": "xx",
                        "SpecifiedPrice": "xx",
                        "Discount": "xx",
                        "OriginalCostWithRI": "xx",
                        "InstanceType": "xx",
                        "TimeUnitName": "xx",
                        "ComponentCode": "xx",
                        "SinglePrice": "xx",
                        "ContractPrice": "xx",
                        "UsedAmountUnit": "xx",
                        "ItemCodeName": "xx",
                        "VoucherPayAmount": "xx",
                        "RiTimeSpan": "xx",
                        "SPDeductionRate": "xx",
                        "PriceUnit": "xx",
                        "ComponentCodeName": "xx",
                        "ItemCode": "xx",
                        "Cost": "xx",
                        "IncentivePayAmount": "xx",
                        "UsedAmount": "xx",
                        "OriginalCostWithSP": "xx"
                    }
                ],
                "FeeEndTime": "2020-09-22 00:00:00",
                "ProductCodeName": "xx",
                "ActionTypeName": "xx",
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ResourceId": "xx",
                "RegionId": "xx",
                "ActionType": "xx",
                "ResourceName": "xx",
                "RegionName": "xx",
                "ProductCode": "xx",
                "ProjectId": 0,
                "OwnerUin": "xx",
                "BillId": "xx",
                "PayerUin": "xx",
                "OperateUin": "xx",
                "BusinessCodeName": "xx",
                "OrderId": "xx",
                "ProjectName": "xx",
                "FeeBeginTime": "2020-09-22 00:00:00",
                "PayModeName": "xx",
                "PayTime": "2020-09-22 00:00:00",
                "ZoneName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

