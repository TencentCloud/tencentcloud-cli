**Example 1: 获取账单明细**

获取账单明细

Input: 

```
tccli billing DescribeBillDetailForOrganization --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Month 2023-08 \
    --NeedRecordNum 1 \
    --ResourceId nat-ftuh6xel
```

Output: 
```
{
    "Response": {
        "Context": "TQpr+vp4d9EeM04pEI6ryHAVS3ZI84mbSVbUzlTD1F8EzZ6vYfNp+wKVhGw0dGkA2iAr5lSGYE4O+bTWApdUY6ZcLDZGpQVYCVApRrjx0IUf6NJGoV8FXlYLQxABqcSt",
        "DetailSet": [
            {
                "ActionType": "postpay_deduct_h",
                "ActionTypeName": "按量计费小时结",
                "AssociatedOrder": null,
                "BillId": "20230816400705427744482",
                "BusinessCode": "p_nat",
                "BusinessCodeName": "NAT网关",
                "ComponentSet": [
                    {
                        "BlendedDiscount": "0.68040500",
                        "CashPayAmount": "0.34020250",
                        "ComponentCode": "v_nat_hour_instance",
                        "ComponentCodeName": "实例",
                        "ComponentConfig": [],
                        "ContractPrice": "0.34020250",
                        "Cost": "0.50000000",
                        "DeductedMeasure": "-",
                        "Discount": "0.680405",
                        "IncentivePayAmount": "0",
                        "InstanceType": "",
                        "ItemCode": "sv_nat_hour_instance_small",
                        "ItemCodeName": "NAT网关-小型实例",
                        "OriginalCostWithRI": "0.00000000",
                        "OriginalCostWithSP": "0.00000000",
                        "PriceUnit": "元/100个/小时",
                        "RealCost": "0.34020250",
                        "RealTotalMeasure": "-",
                        "ReduceType": "折扣",
                        "RiTimeSpan": "0.00000000",
                        "SPDeduction": "0.00000000",
                        "SPDeductionRate": "0.00000000",
                        "SinglePrice": "0.50000000",
                        "SpecifiedPrice": "0.50000000",
                        "TimeSpan": "1",
                        "TimeUnitName": "小时",
                        "TransferPayAmount": "0",
                        "UsedAmount": "100",
                        "UsedAmountUnit": "个",
                        "VoucherPayAmount": "0"
                    }
                ],
                "FeeBeginTime": "2023-08-16 20:00:00",
                "FeeEndTime": "2023-08-16 20:59:59",
                "Formula": "-",
                "FormulaUrl": "https://buy.cloud.tencent.com/price/nat",
                "OperateUin": "700000686592",
                "OrderId": "20230816867705427744432",
                "OwnerUin": "700000686592",
                "PayModeName": "按量计费",
                "PayTime": "2023-08-16 21:15:38",
                "PriceInfo": [],
                "ProductCode": "sp_nat",
                "ProductCodeName": "NAT网关",
                "ProjectId": 0,
                "ProjectName": "默认项目",
                "RegionId": "4",
                "RegionName": "华东地区（上海）",
                "ResourceId": "nat-ftuh6xel",
                "ResourceName": "migration-nat-test3",
                "Tags": [],
                "ZoneName": "其他"
            }
        ],
        "RequestId": "48f32947-8ef2-40b3-94ef-b8c08fc030da",
        "Total": 544
    }
}
```

