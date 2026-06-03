**Example 1: 获取周、半月、月扫码数据**



Input: 

```
tccli trp DescribeFlavorKingCycleBrandImportantProvinceScanAnalysis --cli-unfold-argument  \
    --CorpId 10046 \
    --TypeDate month \
    --QueryDate 2025-04-30 \
    --ProvinceList 湖南
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "0ae9eb9a-67ee-460e-9582-91448f39b39c"
    }
}
```

