**Example 1: 获取周、半月、月品牌城市扫码数据**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandImportantCityScanAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --TypeDate week \
    --QueryDate 2026-04-26
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "City": "上海",
                "GrowRatio": 0.1261,
                "LastCycleMarketShare": 0.7968,
                "LastCycleOtherMarketShare": 0.2032,
                "LastCycleRatio": 0.0169,
                "MarketShare": 0.8249,
                "OtherGrowRatio": -0.0625,
                "OtherMarketShare": 0.1751,
                "Ratio": 0.0161,
                "Regions": [
                    {
                        "GrowRatio": 0.1323,
                        "LastCycleMarketShare": 0.8123,
                        "LastCycleOtherMarketShare": 0.1877,
                        "LastCycleRatio": 0.1036,
                        "MarketShare": 0.8352,
                        "OtherGrowRatio": -0.0334,
                        "OtherMarketShare": 0.1648,
                        "Ratio": 0.1042,
                        "Region": "嘉定区"
                    }
                ]
            }
        ],
        "RequestId": "42a3b034-9cee-4286-b2ca-e146411a9b14"
    }
}
```

