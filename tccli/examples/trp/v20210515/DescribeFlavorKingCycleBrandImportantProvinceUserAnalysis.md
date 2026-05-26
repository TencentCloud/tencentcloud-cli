**Example 1: 获取周、半月、月品牌省用户数据**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandImportantProvinceUserAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --TypeDate month \
    --QueryDate 2026-04-30 \
    --ProvinceList 广东
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cities": [
                    {
                        "City": "东莞",
                        "GrowRatio": 0,
                        "MarketShare": 0,
                        "OtherGrowRatio": 0,
                        "OtherMarketShare": 0
                    }
                ],
                "GrowRatio": 0,
                "MarketShare": 0,
                "OtherGrowRatio": 0,
                "OtherMarketShare": 0,
                "Province": "广东"
            }
        ],
        "RequestId": "4ab28b10-2480-438c-bbea-2102e04a3401"
    }
}
```

