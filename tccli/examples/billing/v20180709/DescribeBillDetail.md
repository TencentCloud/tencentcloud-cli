**Example 1: Getting bill details**



Input: 

```
tccli billing DescribeBillDetail --cli-unfold-argument  \
    --Month 2018-07\
    --PeriodType byPayTime\
    --Offset 0\
    --Limit 1\
    --BeginTime '2018-11-01 00:00:00'\
    --EndTime '2018-11-01 23:59:59'\
    --NeedRecordNum 1\
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
            "PayModeName": "Pay-as-you-go",
            "ProjectName": "Default project",
            "RegionName": "South China (Guangzhou)",
            "ZoneName": "-",
            "ResourceId": "huiyan_idbankcard-1251006373-201907",
            "ResourceName": "-",
            "ActionTypeName": "monthly settlement",
            "BusinessCode": "p_ai_image_huiyan",
            "ProductCode": "sp_ai_image_huiyan_idbankcard",
            "ActionType": "postpay_deduct_m",
            "OrderId": "201907",
            "BillId": "20190612020000003179923224518398",
            "PayTime": "2019-06-12 14:56:05",
            "FeeBeginTime": "2019-06-01 00:00:00",
            "FeeEndTime": "2019-06-30 23:59:59",
            "RegionId": "1",
            "ComponentSet": [
                {
                    "ComponentCodeName": "Three bank card identifiers",
                    "ItemCodeName": "FaceID - three bank card identifiers",
                    "ItemCode": "sv_ai_image_huiyan_idbankcard",
                    "ComponentCode": "v_ai_image_huiyan_idbankcard",
                    "SinglePrice": "0.4",
                    "ContractPrice": "0.4",
                    "SpecifiedPrice": "0.4",
                    "PriceUnit": "USD/count/month",
                    "UsedAmount": "5",
                    "UsedAmountUnit": "count",
                    "TimeSpan": "1",
                    "TimeUnitName": "Month",
                    "Cost": "2",
                    "Discount": "1",
                    "ReduceType": "Discount",
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

