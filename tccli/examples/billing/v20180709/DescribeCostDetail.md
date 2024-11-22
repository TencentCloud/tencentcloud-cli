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
                "PayerUin": "10002011014",
                "BusinessCodeName": "COS 对象存储",
                "ProductCodeName": "COS 流量",
                "PayModeName": "按量计费",
                "ProjectName": "默认项目",
                "RegionName": "华南地区（广州）",
                "ZoneName": "其他",
                "ResourceId": "cpn-dev-238-ap-beijing-1000000086",
                "ResourceName": "cpn-dev-238-ap-beijing",
                "ActionTypeName": "按量计费日结",
                "OrderId": "20211009400006732337101",
                "BillId": "2021100940000673233",
                "FeeBeginTime": "2021-11-03 00:00:00",
                "FeeEndTime": "2021-11-03 23:59:59",
                "ComponentSet": [
                    {
                        "ComponentCodeName": "外网下行流量",
                        "ItemCodeName": "COS 外网下行流量",
                        "SinglePrice": "0.50000000",
                        "PriceUnit": "元/GB/天",
                        "UsedAmount": "0.0020975",
                        "UsedAmountUnit": "GB",
                        "Cost": "0.00104875",
                        "Discount": "1",
                        "RealCost": "0.00104875",
                        "VoucherPayAmount": "0",
                        "CashPayAmount": "0.00104875",
                        "IncentivePayAmount": "0"
                    }
                ],
                "ProductCode": "sp_cos_bw"
            }
        ],
        "Total": 1,
        "RequestId": "51db5fda-deac-4d51-8464-d23c32791abd"
    }
}
```

