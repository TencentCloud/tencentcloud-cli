**Example 1: 获取按地域汇总消耗详情**

获取按地域汇总消耗详情

Input: 

```
tccli billing DescribeCostSummaryByRegion --cli-unfold-argument  \
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
        "RecordNum": 0,
        "Total": {
            "RealTotalCost": "91.04"
        },
        "Data": [
            {
                "RegionId": "18",
                "RegionName": "Asia Pacific (Seoul)",
                "RealTotalCost": "67.00",
                "CashPayAmount": "66.99654091",
                "VoucherPayAmount": "0.00000000",
                "IncentivePayAmount": "0.00000000",
                "TransferPayAmount": "0.00000000",
                "Trend": {
                    "Type": "none",
                    "Value": null
                },
                "Business": [
                    {
                        "BusinessCode": "p_cos",
                        "BusinessCodeName": "Cloud Object Storage",
                        "RegionName": "Asia Pacific (Seoul)",
                        "RealTotalCost": "66.99654091",
                        "CashPayAmount": "66.99654091",
                        "IncentivePayAmount": "0.00000000",
                        "VoucherPayAmount": "0.00000000",
                        "TransferPayAmount": "0.00000000",
                        "Trend": {
                            "Type": "none",
                            "Value": null
                        }
                    }
                ]
            }
        ],
        "RequestId": "cdf3ef28-5ec7-4915-9cc8-a07210dc1f28"
    }
}
```

