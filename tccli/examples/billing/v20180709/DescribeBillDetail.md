**Example 1: 获取账单明细**



Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Month 2018-07 \
    --PeriodType byPayTime \
    --Offset 0 \
    --Limit 1 \
    --BeginTime '2018-11-01 00:00:00' \
    --EndTime '2018-11-01 23:59:59' \
    --NeedRecordNum 1 \
    --ResourceId ins-49zhx6z1
```

Output: 
```
{
    "Response": {
        "DetailSet": {
            "PayerUin": "20548499",
            "OwnerUin": "20548499",
            "OperateUin": "20548499",
            "BusinessCodeName": "人脸核身-云智慧眼",
            "ProductCodeName": "银行卡信息核验",
            "PayModeName": "按量计费",
            "ProjectName": "默认项目",
            "RegionName": "华南地区（广州）",
            "ZoneName": "-",
            "ResourceId": "huiyan_idbankcard-1251006373-201907",
            "ResourceName": "-",
            "ActionTypeName": "月结",
            "OrderId": "201907",
            "BillId": "20190612020000003179923224518398",
            "PayTime": "2019-06-12 14:56:05",
            "FeeBeginTime": "2019-06-01 00:00:00",
            "FeeEndTime": "2019-06-30 23:59:59",
            "RegionId": 1,
            "ComponentSet": [
                {
                    "ComponentCodeName": "银行卡三要素",
                    "ItemCodeName": "人脸核身·云智慧眼-银行卡三要素",
                    "SinglePrice": "0.4",
                    "ContractPrice": "0.4",
                    "SpecifiedPrice": "0.4",
                    "PriceUnit": "元/次/月",
                    "UsedAmount": "5",
                    "UsedAmountUnit": "次",
                    "TimeSpan": "1",
                    "TimeUnitName": "月",
                    "Cost": "2",
                    "Discount": "1",
                    "ReduceType": "折扣",
                    "RealCost": "2",
                    "VoucherPayAmount": "0",
                    "CashPayAmount": "2",
                    "IncentivePayAmount": "0"
                }
            ],
            "Tags": [
                {
                    "TagKey": "-",
                    "TagValue": "-"
                }
            ]
        },
        "Total": 1,
        "RequestId": "d11d7149-3a4a-496c-999a-9287adf0962e"
    }
}
```

