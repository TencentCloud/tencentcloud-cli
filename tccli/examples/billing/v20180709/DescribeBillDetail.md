**Example 1: 获取账单明细**



Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Month 2018-07 \
    --PeriodType byPayTime \
    --Offset 0 \
    --Limit 1 \
    --BeginTime 2018-11-0100:00:00 \
    --EndTime 2018-11-0123:59:59 \
    --NeedRecordNum 1 \
    --ResourceId ins-49zhx6z1
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
                        "ItemCodeName": "xx",
                        "TimeUnitName": "xx",
                        "TimeSpan": "xx",
                        "SinglePrice": "xx",
                        "VoucherPayAmount": "xx",
                        "SpecifiedPrice": "xx",
                        "PriceUnit": "xx",
                        "ComponentCodeName": "xx",
                        "Discount": "xx",
                        "ItemCode": "xx",
                        "Cost": "xx",
                        "IncentivePayAmount": "xx",
                        "CashPayAmount": "xx",
                        "UsedAmount": "xx",
                        "ContractPrice": "xx",
                        "RealCost": "xx",
                        "ComponentCode": "xx",
                        "UsedAmountUnit": "xx"
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

