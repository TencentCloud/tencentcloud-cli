**Example 1: 获取周、半月、月品牌扫描数据**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandScanAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --TypeDate month \
    --QueryDate 2026-04-30
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 107253136,
            "CycleOverCycle": -0.1399,
            "CycleRatio": 0.7009,
            "CycleRatioItems": [
                {
                    "BrandName": "伍子醉",
                    "Duration": "20260301-20260331",
                    "Ratio": 0.2956
                }
            ]
        },
        "RequestId": "bc52b11a-1d96-411b-a085-f153cdc07ac3"
    }
}
```

