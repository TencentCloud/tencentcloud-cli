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
        "DetailSet": {
            "PayerUin": "20548499",
            "BusinessCodeName": "人脸核身-云智慧眼",
            "ProductCodeName": "人脸核身·云智慧眼-银行卡信息核验",
            "PayModeName": "按量计费",
            "ProjectName": "默认项目",
            "RegionName": "华南地区（广州）",
            "ZoneName": "-",
            "ResourceName": "-",
            "ActionTypeName": "月结",
            "OrderId": "201907",
            "BillId": "20190612020000003179923224518398",
            "FeeBeginTime": "2019-06-01 00:00:00",
            "FeeEndTime": "2019-06-30 23:59:59",
            "ProductCode": "sp_ai_image_huiyan_idbankcard",
            "ComponentSet": [
                {
                    "ComponentCodeName": "银行卡三要素",
                    "ItemCodeName": "人脸核身·云智慧眼-银行卡三要素",
                    "SinglePrice": "0.4",
                    "PriceUnit": "元/次/月",
                    "UsedAmount": "5",
                    "UsedAmountUnit": "次",
                    "Cost": "2",
                    "Discount": "1",
                    "RealCost": "2",
                    "VoucherPayAmount": "0",
                    "CashPayAmount": "2",
                    "IncentivePayAmount": "0"
                }
            ]
        },
        "Total": 1,
        "RequestId": "d11d7149-3a4a-496c-999a-9287adf0962e"
    }
}
```

