**Example 1: 查询消耗明细数据**



Input: 

```
tccli billing DescribeCostDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --BeginTime '2018-11-01 00:00:00' \
    --EndTime '2018-11-01 23:59:59' \
    --NeedRecordNum 1
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "PayerUin": "abc",
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
                "BillId": "abc",
                "FeeBeginTime": "abc",
                "FeeEndTime": "abc",
                "ComponentSet": [
                    {
                        "ComponentCodeName": "abc",
                        "ItemCodeName": "abc",
                        "SinglePrice": "abc",
                        "PriceUnit": "abc",
                        "UsedAmount": "abc",
                        "UsedAmountUnit": "abc",
                        "Cost": "abc",
                        "Discount": "abc",
                        "RealCost": "abc",
                        "VoucherPayAmount": "abc",
                        "CashPayAmount": "abc",
                        "IncentivePayAmount": "abc"
                    }
                ],
                "ProductCode": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

