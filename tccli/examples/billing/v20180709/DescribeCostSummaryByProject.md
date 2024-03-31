**Example 1: 获取按项目汇总消耗详情**

获取按项目汇总消耗详情

Input: 

```
tccli billing DescribeCostSummaryByProject --cli-unfold-argument  \
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
            "RealTotalCost": "abc"
        },
        "Data": [
            {
                "ProjectId": "abc",
                "ProjectName": "abc",
                "RealTotalCost": "abc",
                "Trend": {
                    "Type": "abc",
                    "Value": "abc"
                },
                "Business": [
                    {
                        "BusinessCode": "abc",
                        "BusinessCodeName": "abc",
                        "RealTotalCost": "abc",
                        "Trend": {
                            "Type": "abc",
                            "Value": "abc"
                        },
                        "CashPayAmount": "abc",
                        "IncentivePayAmount": "abc",
                        "VoucherPayAmount": "abc",
                        "TransferPayAmount": "abc"
                    }
                ],
                "CashPayAmount": "abc",
                "IncentivePayAmount": "abc",
                "VoucherPayAmount": "abc",
                "TransferPayAmount": "abc"
            }
        ],
        "RecordNum": 1,
        "RequestId": "abc"
    }
}
```

