**Example 1: 云资源配置风险统计**



Input: 

```
tccli csip DescribeCFGRiskStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CFGRiskStatistics": {
            "AssetViewAddCount": 257,
            "AssetViewCount": 311,
            "CheckViewAddCount": 36,
            "CheckViewCount": 36,
            "HighPriorityAssetViewCount": 80,
            "HighPriorityCheckViewCount": 9,
            "HighPriorityRiskCount": 112,
            "RiskAddCount": 349,
            "TotalRiskCount": 349
        },
        "RequestId": "0d5d3754-cf50-40e4-b710-d9a913cc3674"
    }
}
```

