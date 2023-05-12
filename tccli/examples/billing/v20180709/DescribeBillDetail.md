**Example 1: 获取账单明细**

获取账单明细

Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --PeriodType byUsedTime \
    --Month 2022-01 \
    --BeginTime 2022-01-01 00:00:00 \
    --EndTime 2022-01-02 00:00:00 \
    --NeedRecordNum 1 \
    --ResourceId eip-ct36wgjp
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "ActionType": "postpay_deduct_h",
                "ActionTypeName": "按量计费小时结",
                "BillId": "20220101400113231274762",
                "BusinessCode": "p_eip",
                "BusinessCodeName": "公网 IP",
                "ComponentSet": [
                    {
                        "BlendedDiscount": "-",
                        "CashPayAmount": "0.00040000",
                        "ComponentCode": "v_eip_traffic",
                        "ComponentCodeName": "公网网络-流量",
                        "ContractPrice": "0.00022222",
                        "Cost": "0",
                        "Discount": "0",
                        "IncentivePayAmount": "0",
                        "InstanceType": "0",
                        "ItemCode": "sv_eip_traffic",
                        "ItemCodeName": "公网IP-按流量计费",
                        "OriginalCostWithRI": "0.00000000",
                        "OriginalCostWithSP": "0.00000000",
                        "PriceUnit": "元/GB/秒",
                        "RealCost": "0.00040000",
                        "ReduceType": "折扣",
                        "RiTimeSpan": "0.00000000",
                        "SPDeduction": "0.00000000",
                        "SPDeductionRate": "0.00000000",
                        "SinglePrice": "0",
                        "SpecifiedPrice": "0",
                        "TimeSpan": "3600",
                        "TimeUnitName": "秒",
                        "UsedAmount": "0.0005",
                        "UsedAmountUnit": "GB",
                        "VoucherPayAmount": "0"
                    }
                ],
                "FeeBeginTime": "2022-01-01 00:00:00",
                "FeeEndTime": "2022-01-01 00:59:59",
                "OperateUin": "90xxxxx00",
                "OrderId": "eip-ctgjp",
                "OwnerUin": "90xxxxx00",
                "PayModeName": "按量计费",
                "PayTime": "2022-01-01 01:26:04",
                "PayerUin": "90xxxxx00",
                "PriceInfo": [],
                "ProductCode": "sp_eip",
                "ProductCodeName": "公网 IP",
                "ProjectId": 1203241,
                "ProjectName": "测试项目",
                "RegionId": "4",
                "RegionName": "华东地区（上海）",
                "ResourceId": "eip-cxxgjp",
                "ResourceName": "",
                "Tags": [],
                "ZoneName": "其他"
            }
        ],
        "RequestId": "920fb001-3145-4af1-96c1-246cce80bba1",
        "Context": "UEEJBfSsteS7dZgAaEEziWS40d4sn4urG7",
        "Total": 25
    }
}
```

