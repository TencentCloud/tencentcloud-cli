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
        "RequestId": "a63a68af-fb44-4d2f-8595-5269a9e69876",
        "ResourceSummarySet": [
            {
                "ActionTypeName": "按量计费日结",
                "BusinessCode": "p_yunjing",
                "BusinessCodeName": "T-Sec-主机安全（CWP）",
                "CashPayAmount": "16.20000000",
                "ConfigDesc": "主机安全/专业版: 1 个",
                "Discount": "0.3",
                "ExtendField1": "-",
                "ExtendField2": "-",
                "ExtendField3": "-",
                "ExtendField4": "-",
                "ExtendField5": "-",
                "FeeBeginTime": "2022-01-13 00:00:00",
                "FeeEndTime": "2022-01-31 23:59:59",
                "IncentivePayAmount": "0.00000000",
                "InstanceType": "-",
                "OperateUin": "90xxxxx00",
                "OrderId": "-",
                "OriginalCostWithRI": "0.00000000",
                "OriginalCostWithSP": "0.00000000",
                "OwnerUin": "90xxxxx00",
                "PayModeName": "按量计费",
                "PayTime": "0000-00-00 00:00:00",
                "PayerUin": "90xxxxx00",
                "ProductCode": "sp_yunjing_vip",
                "ProductCodeName": "主机安全/专业防护",
                "ProjectName": "默认项目",
                "RealTotalCost": "17.10000000",
                "ReduceType": "折扣",
                "RegionId": 1,
                "RegionName": "华南地区（广州）",
                "ResourceId": "0-0xxd9-1ab4-4d6d-b38a-axx0fa4e-172.16.64.12",
                "ResourceName": "",
                "SPDeduction": "0.00000000",
                "Tags": [],
                "TotalCost": "57",
                "VoucherPayAmount": "0.90000000",
                "ZoneName": "其他"
            }
        ],
        "Total": 465
    }
}
```

