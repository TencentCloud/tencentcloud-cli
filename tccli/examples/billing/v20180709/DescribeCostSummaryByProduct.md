**Example 1: 获取按产品汇总消耗详情**

获取按产品汇总消耗详情

Input: 

```
tccli billing DescribeCostSummaryByProduct --cli-unfold-argument  \
    --NeedRecordNum 1 \
    --EndTime 2018-11 \
    --Limit 1 \
    --BeginTime 2018-11 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "Total": {
            "RealTotalCost": "4.20000000"
        },
        "Data": [
            {
                "BusinessCode": "p_clb",
                "BusinessCodeName": "负载均衡CLB",
                "RealTotalCost": "4.20000000",
                "Trend": {
                    "Type": "upward",
                    "Value": "1.72"
                },
                "CashPayAmount": "4.20000000",
                "IncentivePayAmount": "0.00000000",
                "VoucherPayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "RegionName": "其他"
            }
        ],
        "RecordNum": 1,
        "RequestId": "078ec9c607a2486099e06e04a99502db"
    }
}
```

