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
        "RecordNum": 2,
        "Total": {
            "RealTotalCost": "220.67"
        },
        "Data": [
            {
                "BusinessCode": "p_cvm",
                "BusinessCodeName": "云服务器",
                "RealTotalCost": "220.67",
                "Trend": {
                    "Type": "postPay",
                    "Value": "test"
                }
            }
        ],
        "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
    }
}
```

