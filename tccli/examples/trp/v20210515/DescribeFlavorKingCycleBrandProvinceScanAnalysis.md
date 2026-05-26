**Example 1: 获取周、半月、月品牌省扫码数据**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandProvinceScanAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --TypeDate month \
    --QueryDate 2026-04-30
```

Output: 
```
{
    "Response": {
        "Data": {
            "GrowRatio": -0.1399,
            "LastCycleMarketShare": 0.7044,
            "MarketShare": 0.7009,
            "OtherGrowRatio": -0.1253,
            "Provinces": [
                {
                    "GrowRatio": -0.0496,
                    "LastCycleMarketShare": 0.7917,
                    "LastCycleRatio": 0.0145,
                    "MarketShare": 0.805,
                    "OtherGrowRatio": -0.125,
                    "OtherLastCycleMarketShare": 0.2083,
                    "OtherMarketShare": 0.195,
                    "Province": "上海",
                    "Ratio": 0.016
                }
            ]
        },
        "RequestId": "3111732e-bba2-403e-99f7-b2e2b40a89a1"
    }
}
```

