**Example 1: 获取按产品汇总消耗详情**



Input: 

```
tccli billing DescribeCostSummaryByProduct --cli-unfold-argument  \
    --BeginTime 2018-11 \
    --EndTime 2018-11 \
    --Offset 0 \
    --Limit 1 \
    --NeedRecordNum 1
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
        "RequestId": "xx"
    }
}
```

