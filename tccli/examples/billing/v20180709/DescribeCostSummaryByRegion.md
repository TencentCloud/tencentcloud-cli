**Example 1: 获取按地域汇总消耗详情**



Input: 

```
tccli billing DescribeCostSummaryByRegion --cli-unfold-argument  \
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
        "Total": {
            "RealTotalCost": "510.15"
        },
        "Data": [
            {
                "RegionId": "0",
                "RegionName": "其他",
                "RealTotalCost": "-0.69",
                "Trend": {
                    "Type": "downward",
                    "Value": "xx"
                },
                "Business": [
                    {
                        "BusinessCode": "billVirtualId",
                        "BusinessCodeName": "月度计费精度差异",
                        "RealTotalCost": "-0.69",
                        "Trend": {
                            "Type": "downward",
                            "Value": "0"
                        }
                    }
                ]
            }
        ],
        "RecordNum": 8,
        "Ready": 1,
        "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
    }
}
```

