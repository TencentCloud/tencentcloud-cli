**Example 1: 查询按小时账单明细**



Input: 

```
tccli waf DescribeLLMHourBillDetail --cli-unfold-argument  \
    --InstanceId waf_2112f6ik1700cnkd \
    --Date 2026-01-01
```

Output: 
```
{
    "Response": {
        "InstanceId": "waf_2112f6ik1700cnkd",
        "Date": "2026-01-01",
        "EstimatedTotalFee": "1234.56",
        "ItemFees": {
            "PromptAttackFee": "300.0",
            "ContentTextFee": "500.0",
            "ContentImageFee": "500.0",
            "SensitiveDataFee": "500.0"
        },
        "HourlyTrend": [
            {
                "Hour": "00",
                "Fee": "50.05"
            },
            {
                "Hour": "01",
                "Fee": "50.05"
            }
        ],
        "HourlyDetail": [
            {
                "TimeRange": "00:00-01:00",
                "PromptAttackUsage": 10000,
                "ContentTextUsage": 10000,
                "ContentImageUsage": 10000,
                "SensitiveDataUsage": 0,
                "PromptAttackFee": "0.035",
                "ContentTextFee": "0.015",
                "ContentImageFee": "50.0",
                "SensitiveDataFee": "0.0",
                "TotalFee": "50.05"
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

