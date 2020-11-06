**Example 1: 获取按地域汇总消耗详情**



Input: 

```
tccli billing DescribeCostSummaryByRegion --cli-unfold-argument  \
    --PayerUin 909619400 \
    --BeginTime 2018-11-0100:00:00 \
    --EndTime 2018-11-3023:59:59 \
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
                    "Type": "downward"
                },
                "Business": [
                    {
                        "BusinessCode": "billVirtualId",
                        "BusinessCodeName": "月度计费精度差异",
                        "RealTotalCost": "-0.69",
                        "Trend": {
                            "Type": "downward"
                        }
                    }
                ]
            }
        ],
        "PageSize": 1,
        "PageNo": 1,
        "RecordNum": 8,
        "Ready": 1,
        "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
    }
}
```

